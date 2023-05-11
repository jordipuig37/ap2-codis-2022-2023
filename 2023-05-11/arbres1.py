import yogi as yg
import typing as ty


Arbin = ty.Optional[tuple[int, 'Arbin', 'Arbin']]


def llegir_arbre() -> Arbin:
    """Llegeix un arbre binari recursivament, donat en pre ordre."""
    x = yg.read(int)
    if x != -1:
        return (x, llegir_arbre(), llegir_arbre())
    return None


def print_postordre(arbre: Arbin) -> None:
    """Escriu un arbre binari recursivament en postordre."""
    if arbre is not None:
        print_postordre(arbre[1])
        print_postordre(arbre[2])
        print(" ", arbre[0], end="", sep="")


def print_inordre(arbre: Arbin) -> None:
    """Escriu un arbre binari recursivament en inordre."""
    if arbre is not None:
        print_inordre(arbre[1])
        print(" ", arbre[0], end="", sep="")
        print_inordre(arbre[2])


def main():
    arbre = llegir_arbre()
    print("pos:", end="")
    print_postordre(arbre)
    print()
    print("ino:", end="")
    print_inordre(arbre)
    print()


if __name__ == "__main__":
    main()
