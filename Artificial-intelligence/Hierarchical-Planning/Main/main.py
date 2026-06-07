# Mengimpor class HLA dan PlanProblem dari modul ai_pkg.planning
from ai_pkg.planning import HLA, Problem as PlanProblem

# Library berisi definisi aksi hierarkis (HLA),
# langkah detail (refinement), precondition, dan effect
library = {

    # Daftar aksi tingkat tinggi (High Level Action)
    'HLA': [
        'Go(Home,Airport)',                 # Aksi abstrak pergi ke bandara
        'Go(Home,Airport)',                 # Alternatif lain aksi yang sama
        'Drive(Home,AirportParking)',       # Aksi detail: mengemudi ke parkiran bandara
        'Shuttle(AirportParking,Airport)', # Aksi detail: naik shuttle ke bandara
        'Taxi(Home,Airport)'                # Aksi detail: naik taksi ke bandara
    ],

    # Refinement / dekomposisi aksi
    # Menjelaskan bagaimana aksi abstrak dipecah menjadi langkah lebih detail
    'steps': [

        # Cara pertama ke bandara:
        # Mengemudi lalu naik shuttle
        [
            'Drive(Home,AirportParking)',
            'Shuttle(AirportParking,Airport)'
        ],

        # Cara kedua:
        # Langsung naik taksi
        [
            'Taxi(Home,Airport)'
        ],

        # Aksi detail tidak memiliki langkah turunan lagi
        [],
        [],
        []
    ],

    # Syarat sebelum aksi bisa dilakukan
    'precond': [

        # Untuk "Go(Home,Airport)" versi mobil:
        # Harus berada di rumah dan punya mobil
        ['At(Home) & Have(Car)'],

        # Untuk "Go(Home,Airport)" versi taksi:
        # Harus berada di rumah
        ['At(Home)'],

        # Untuk mengemudi:
        # Harus di rumah dan punya mobil
        ['At(Home) & Have(Car)'],

        # Untuk naik shuttle:
        # Harus berada di parkiran bandara
        ['At(AirportParking)'],

        # Untuk naik taksi:
        # Harus berada di rumah
        ['At(Home)']
    ],

    # Effect = perubahan kondisi setelah aksi dilakukan
    'effect': [

        # Setelah berhasil pergi ke bandara:
        # Posisi di bandara dan tidak lagi di rumah
        ['At(Airport) & ~At(Home)'],

        # Setelah naik taksi:
        # Sampai di bandara, tidak di rumah, dan uang cash habis
        ['At(Airport) & ~At(Home) & ~Have(Cash)'],

        # Setelah mengemudi:
        # Sampai di parkiran bandara
        ['At(AirportParking) & ~At(Home)'],

        # Setelah naik shuttle:
        # Sampai di bandara
        ['At(Airport) & ~At(LongTermParking)'],

        # Setelah naik taksi:
        # Sampai di bandara dan uang cash habis
        ['At(Airport) & ~At(Home) & ~Have(Cash)']
    ]
}

# Membuat High Level Action (aksi abstrak)
goto_airport = HLA('Go(Home,Airport)')

# Membuat planning problem
problem = PlanProblem(

    # Initial state / kondisi awal
    # Sedang di rumah, punya uang cash, dan punya mobil
    'At(Home) & Have(Cash) & Have(Car)',

    # Goal state / tujuan akhir
    # Harus sampai di bandara dan masih punya cash
    'At(Airport) & Have(Cash)',

    # Daftar aksi awal yang ingin dilakukan
    [goto_airport]
)

# Menjalankan hierarchical planning search
# Sistem akan mencari urutan aksi yang memenuhi goal
solution = PlanProblem.hierarchical_search(problem, library)

# Menampilkan hasil solusi planning
for step in solution:

    # Menampilkan precondition dari aksi
    print("precondition :", step.precond)

    # Menampilkan nama aksi
    print("action       :", step.name)

    # Menampilkan effect dari aksi
    print("effect       :", step.effect)

    print()