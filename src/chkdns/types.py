import click
from validators import domain  # type: ignore


class DOMAIN(click.ParamType):
    name = "domain"

    def convert(self, value, param, ctx):
        if not isinstance(value, tuple):
            valid = domain(value)
            if not valid:
                self.fail(
                    f"{value} is not a valid domain.",
                    param,
                    ctx,
                )

        return value
