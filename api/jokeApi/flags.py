from dataclasses import dataclass
from config import FLAG_PREFIX


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

    async def BuildString(self, separator: str = ", "):
        data = await self.GetFlagData()
        current_flags: list = []
        for flag, boolean in data:
            if not boolean:
                continue
            current_flags.append(flag.capitalize())
        return separator.join(current_flags)

    def __bool__(self):
        if self.nsfw:
            return True
        if self.religious:
            return True
        if self.political:
            return True
        if self.racist:
            return True
        if self.sexist:
            return True
        if self.explicit:
            return True
        return False

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
                       any_flag: str = f"{FLAG_PREFIX}any",
                       nsfw_flag: str = f"{FLAG_PREFIX}nsfw",
                       religious_flag: str = f"{FLAG_PREFIX}religious",
                       political_flag: str = f"{FLAG_PREFIX}political",
                       racist_flag: str = f"{FLAG_PREFIX}racist",
                       sexist_flag: str = f"{FLAG_PREFIX}sexist",
                       explicit_flag: str = f"{FLAG_PREFIX}explicit"):
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
