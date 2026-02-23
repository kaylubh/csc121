#
# Caleb Hemphill
# 02/23/2026
# Assignment Score Log / Calculator
#

def main():
    # Step A - Ashley, 3 scores
    print("Please enter Ashley's scores one by one.")
    a_list = [int(input('Enter a score: ')) for _ in range(3)]
    print(f"Ashley's scores: {a_list}")
    print('')

    # Step B - Barb, 5 scores
    print("Please enter Barb's scores one by one.")
    b_list = [int(input('Enter a score: ')) for _ in range(5)]
    print(f"Barb's scores: {b_list}")
    print('')

    # Step C - Carl, 4 scores
    print("Please enter Carl's scores one by one.")
    c_list = [int(input('Enter a score: ')) for _ in range(4)]
    print(f"Carl's scores: {c_list}")
    print('')

    # Step D - combined scores list
    all_scores = [a_list[:], b_list[:], c_list[:]]
    print(f'All scores: {all_scores}')

    # Step E - add 5% extra credit to all scores
    for scores in all_scores:
        for i in range(len(scores)):
            scores[i] = int(scores[i] * 1.05)

    print(f'All scores after extra credit: {all_scores}')

    # Step F - score spreads
    score_spreads = []
    for scores in all_scores:
        score_spreads.append(max(scores) - min(scores))

    print(f'Score spreads: {score_spreads}')
    print('')

    # Step G - original lists
    print(f"Ashley's scores: {a_list}")
    print(f"Barb's scores: {b_list}")
    print(f"Carl's scores: {c_list}")


if __name__ == '__main__':
    main()
