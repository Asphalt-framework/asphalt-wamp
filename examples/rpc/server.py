"""This example demonstrates how to register a remote procedure handler with WAMP."""

import logging

from asphalt.core import ContainerComponent, Context, run_application


def uppercase(ctx, message: str):
    return message.upper()


class RPCServerComponent(ContainerComponent):
    async def start(self, ctx: Context):
        self.add_component('wamp', url='ws://localhost:8080')
        await super().start(ctx)

        await ctx.wamp.register_procedure(uppercase, 'uppercase')

run_application(RPCServerComponent(), logging=logging.INFO)
