"""Módulo com funções."""


def is_prime(number: int) -> bool:
    """Retorna True se o número for primo e False caso contrário."""
    if number <= 0:
        return False
    else:
        contador = 2
        while(contador < number):
            if number % contador == 0:
                return False
            contador += 1
        return True


def proximo_primo(number:int) -> int:
    while True:
        if is_prime(number+1):
            return number+1
        else:
            number += 1


def list_prime_factors(number: int) -> list[int]:
    """Retorna uma lista com os fatores primos de cada número da lista fornecida."""
    list_primes = []
    primeiros_primos = [2]
    while number != 1:
        dividiu = False
        for i in primeiros_primos:
            if number % i == 0:
                number = number / i
                list_primes.append(i)
                dividiu = True
                break
        if not dividiu:
            proximo = proximo_primo(primeiros_primos[-1])
            primeiros_primos.append(proximo)
            
    return list_primes