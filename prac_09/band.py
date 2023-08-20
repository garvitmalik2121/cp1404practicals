class Band:
    """Band class for storing details of a band and its musicians."""

    def __init__(self, name):
        """Initialize a Band."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        musician_details = []
        for musician in self.musicians:
            musician_details.append(f"{musician.name} ({musician.instruments})")
        return f"{self.name} ({', '.join(musician_details)})"

    def add_musician(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play_music(self):
        """Return a string showing each musician playing their first (or no) instrument."""
        play_output = []
        for musician in self.musicians:
            play_output.append(musician.play())
        return "\n".join(play_output)


if __name__ == '__main__':
    from guitar import Guitar
    from musician import Musician

    my_band = Band("Extreme")
    nuno_bettencourt = Musician("Nuno Bettencourt")
    nuno_bettencourt.add(Guitar("Washburn N4", 1990, 2499.95))
    nuno_bettencourt.add(Guitar("Takamine acoustic", 1986, 1200.0))
    my_band.add_musician(nuno_bettencourt)
    my_band.add_musician(Musician("Gary Cherone"))
    pat_badger = Musician("Pat Badger")
    pat_badger.add(Guitar("Mouradian CS-74 Bass", 2009, 1500.0))
    my_band.add_musician(pat_badger)
    kevin_figueiredo = Musician("Kevin Figueiredo")
    my_band.add_musician(kevin_figueiredo)

    print("band (str)")
    print(my_band)
    assert str(my_band) == "Extreme (Nuno Bettencourt ([Washburn N4 (1990) : $2,499.95, Takamine acoustic (1986) : $1,200.00]), Gary Cherone ([]), Pat Badger ([Mouradian CS-74 Bass (2009) : $1,500.00]), Kevin Figueiredo ([]))"

    print("band.play_music()")
    print(my_band.play_music())
    assert my_band.play_music() == "Nuno Bettencourt is playing: Washburn N4 (1990) : $2,499.95\nGary Cherone needs an instrument!\nPat Badger is playing: Mouradian CS-74 Bass (2009) : $1,500.00\nKevin Figueiredo needs an instrument!"
