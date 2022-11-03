import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    result = re.search(r"^([0-9]{2}|[0-9]{1}):?([0-9]{2})?\s(AM|PM)(\sto\s)([0-9]{2}|[0-9]{1}):?([0-9]{2})?\s(AM|PM)$", s, re.IGNORECASE)
    if not result:
        raise ValueError
    else:
        start_hour = result.group(1)
        start_minute = result.group(2)
        group_3 = result.group(3) # AM or PM
        group_4 = result.group(4) # \sto\s
        end_hour = result.group(5)
        end_minute = result.group(6)
        group_7 = result.group(7) # AM or PM


        if group_3 == "PM":
            start_hour = int(start_hour) + 12
        elif group_3 == "AM" and int(start_hour) == 12:
            start_hour = 00
        elif group_7 == "PM" and int(end_hour) < 12:
            end_hour = int(end_hour) + 12


        if start_minute and end_minute:
            if int(start_minute) < 60 and int(end_minute) < 60:
                if group_3 == "AM" and int(start_hour) < 10:
                    return f"{int(start_hour):02}:{start_minute}{group_4}{end_hour}:{end_minute}"
                elif group_7 == "AM" and int(end_hour) < 10:
                    return f"{start_hour}:{start_minute}{group_4}{int(end_hour):02}:{end_minute}"
                else:
                    return f"{start_hour}:{start_minute}{group_4}{int(end_hour)}:{end_minute}"
            else:
                raise ValueError
        else:
            if group_3 == "AM" and int(start_hour) < 10:
                return f"{int(start_hour):02}:00{group_4}{end_hour}:00"
            elif group_7 == "AM" and int(end_hour) < 10:
                return f"{start_hour}:00{group_4}{int(end_hour):02}:00"
            else:
                return f"{start_hour}:00{group_4}{int(end_hour)}:00"


if __name__ == "__main__":
    main()