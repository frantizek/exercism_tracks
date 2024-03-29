def primes(limit: int) -> list[int]:
    valid_primes = [x for x in range(2, limit+1)]
    for number in valid_primes:
        for temporal_index in range(number, limit+1):
            if number*temporal_index in valid_primes:
                valid_primes.remove(number*temporal_index)
    return valid_primes


def main():
    print(primes(200))


if __name__ == '__main__':
    main()
