# Shell Sort (Better performance than insertion sort)

import time


def sort(arr: list) -> list:
    gap = 1

    while gap < len(arr) / 3:
        gap = gap * 3 + 1

    while gap > 0:
        for i in range(gap, len(arr)):
            for j in range(i, 0, -gap):
                if arr[j] < arr[j - gap]:
                    arr[j], arr[j - gap] = arr[j - gap], arr[j]
                    if gap != 1:
                        break
                else:
                    break
        gap //= 3

    return arr


start = time.perf_counter()
print(
    sort(
        [
            73,
            17,
            13,
            66,
            39,
            91,
            56,
            53,
            9,
            31,
            36,
            93,
            48,
            80,
            55,
            84,
            5,
            46,
            64,
            68,
            70,
            40,
            76,
            79,
            29,
            27,
            47,
            41,
            94,
            12,
            23,
            25,
            19,
            60,
            83,
            42,
            99,
            1,
            2,
            72,
            43,
            67,
            74,
            95,
            86,
            57,
            49,
            62,
            81,
            18,
            35,
            90,
            61,
            98,
            75,
            89,
            10,
            37,
            26,
            69,
            52,
            44,
            54,
            11,
            85,
            96,
            51,
            7,
            16,
            24,
            21,
            38,
            97,
            59,
            30,
            65,
            58,
            50,
            77,
            63,
            88,
            82,
            6,
            32,
            20,
            78,
            28,
            22,
            3,
            45,
        ]
    )
)
print("Total time taken : ", time.perf_counter() - start)
