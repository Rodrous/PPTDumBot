from dataclasses import dataclass


@dataclass(frozen=True, slots=True, kw_only=True)
class FlagBlacklist:
    nsfw: bool = False
    religious: bool = False
    political: bool = False
    racist: bool = False
    sexist: bool = False
    explicit: bool = False

    async def GetFlagData(self) -> list[tuple[str, bool]]:
        return [
            ("nsfw", self.nsfw),
            ("religious", self.religious),
            ("political", self.political),
            ("racist", self.racist),
            ("sexist", self.sexist),
            ("explicit", self.explicit)
        ]

    @classmethod
    def Inverse(cls, *,
                nsfw=True,
                religious=True,
                political=True,
                racist=True,
                sexist=True,
                explicit=True):
        return cls(
            nsfw=not nsfw,
            religious=not religious,
            political=not political,
            racist=not racist,
            sexist=not sexist,
            explicit=not explicit
        )

    @classmethod
    async def All(cls):
        return cls(
            nsfw=True,
            religious=True,
            political=True,
            racist=True,
            sexist=True,
            explicit=True
        )

    @classmethod
    async def FromArgs(cls, args: str, *,
                       inverse: bool = False,
                       any_flag: str = "-any",
                       nsfw_flag: str = "-nsfw",
                       religious_flag: str = "-religious",
                       political_flag: str = "-political",
                       racist_flag: str = "-racist",
                       sexist_flag: str = "-sexist",
                       explicit_flag: str = "-explicit"):
        class_creation = cls
        if any_flag in args:
            return class_creation()
        nsfw = nsfw_flag in args
        religious = religious_flag in args
        political = political_flag in args
        racist = racist_flag in args
        sexist = sexist_flag in args
        explicit = explicit_flag in args
        if inverse:
            class_creation = cls.Inverse
        return class_creation(
            nsfw=nsfw,
            religious=religious,
            political=political,
            racist=racist,
            sexist=sexist,
            explicit=explicit
        )
