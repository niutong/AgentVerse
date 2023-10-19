from __future__ import annotations

from typing import TYPE_CHECKING, List

from agentverse.message import Message

from . import selector_registry as SelectorRegistry
from .base import BaseSelector

if TYPE_CHECKING:
    from agentverse.environments import BaseEnvironment


@SelectorRegistry.register("story_generator")
class StoryGeneratorSelector(BaseSelector):
    def select_message(
        self, environment: BaseEnvironment, messages: List[Message]
    ) -> List[Message]:
        selected = []
        for message in messages:
            # selected.append(message)
            if message.content.startswith("[Speak]"):
                selected.append(message)
            elif message.content.startswith("[Listen]"):
                continue
            elif message.content != "" or len(message.tool_response) > 0:
                selected.append(message)

        # If some student speak while the professor is speaking, then
        # we brutely discard the student's message in this turn
        if (
            len(selected) > 1
            and selected[0].sender.startswith("Professor")
            and selected[0].content != ""
        ):
            filtered_selected = []
            filtered_selected.append(selected[0])
            for message in selected[1:]:
                if message.content.startswith("[RaiseHand]"):
                    filtered_selected.append(message)
            selected = filtered_selected
        return selected
