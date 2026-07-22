from ecosystem_foundations.base.registry import GenericRegistry, BaseItemTypeDefinition

EVENT_STATUS_REGISTRY = GenericRegistry[BaseItemTypeDefinition](
    key_fn=lambda d: (d.model, d.code),
)
EVENT_TYPE_REGISTRY = GenericRegistry[BaseItemTypeDefinition](
    key_fn=lambda d: (d.model, d.code),
)
DEADLINE_STATUS_REGISTRY = GenericRegistry[BaseItemTypeDefinition](
    key_fn=lambda d: (d.model, d.code),
)
DEADLINE_TYPE_REGISTRY = GenericRegistry[BaseItemTypeDefinition](
    key_fn=lambda d: (d.model, d.code),
)