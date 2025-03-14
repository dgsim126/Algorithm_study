
    ## 모든 달이 28일이니까 29는 2월 1일, 57은 3월 1일...(즉 범위는 1~336)
    ## 1월1일= 1 -> 1/28= 0월 -> 1%28= 1일 => (0+1)월 1일
    ## 2월18일= 46 -> 46/28= 1월 -> 46%28= 18일 => (1+1)월 18일
    ## 1년은 336 즉 2000년 1월 1일 -> (2000 * 12 * 28)년 (1




def convert_to_days(date):
    year, month, day = map(int, date.split('.'))
    return year * 12 * 28 + (month - 1) * 28 + day


def solution(today, terms, privacies):
    today_days = convert_to_days(today)

    term_dict = {}
    for term in terms:
        term_type, term_duration = term.split()
        term_dict[term_type] = int(term_duration)

    result = []

    for idx, privacy in enumerate(privacies):
        privacy_date, privacy_term = privacy.split()
        collected_days = convert_to_days(privacy_date)
        expiration_days = collected_days + term_dict[privacy_term] * 28 - 1

        if expiration_days < today_days:
            result.append(idx + 1)

    return result


## main ##
today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

print(solution(today, terms, privacies))  # [1, 3]

