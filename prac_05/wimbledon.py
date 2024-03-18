def read_process_csv(file_name):
    with open(file_name, "r", encoding="utf-8-sig") as input_file:
        next(input_file)
        data = [line.strip().split(',') for line in input_file]
    return data


def count_winners(data):
    winners = {}
    for record in data:
        player_name = record[1]
        winners[player_name] = winners.get(player_name, 0) + 1
    return winners


def extract_countries_played(data):
    countries_played = {record[2] for record in data}
    return countries_played


def main(file_name):
    data = read_process_csv(file_name)
    winners = count_winners(data)
    countries_played = extract_countries_played(data)

    print("Wimbledon Winners:")
    for winner, wins in winners.items():
        print(f"{winner}: {wins} wins")

    sorted_countries = sorted(list(countries_played))
    countries_str = ', '.join(sorted_countries)
    print(f"\nThe players in these {len(sorted_countries)} countries have played in Wimbledon:\n{countries_str}")
