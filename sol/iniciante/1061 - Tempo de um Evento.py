# 1061 - Tempo de um Evento
# https://judge.beecrowd.com/pt/problems/view/1061


def main():
    start_day = int(input().split()[-1])
    start_h, start_m, start_s = [int(x) for x in input().split(" : ")]

    end_day = int(input().split()[-1])
    end_h, end_m, end_s = [int(x) for x in input().split(" : ")]

    # convert timestamps to seconds
    starttime_in_seconds = ((start_day * 24 + start_h) * 60 + start_m) * 60 + start_s
    endtime_in_seconds = ((end_day * 24 + end_h) * 60 + end_m) * 60 + end_s
    duration_in_seconds = endtime_in_seconds - starttime_in_seconds

    # one day is 86400 seconds
    print(duration_in_seconds // 86400, "dia(s)")
    # one hour is 3600 seconds and so on...
    print((duration_in_seconds % 86400) // 3600, "hora(s)")
    print((duration_in_seconds % 3600) // 60, "minuto(s)")
    print(duration_in_seconds % 60, "segundo(s)")


if __name__ == "__main__":
    main()
