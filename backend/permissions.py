from rest_framework.permissions import BasePermission


class HasPermission(BasePermission):
    required_permissions = []

    def has_permission(self, request, view):
        if not self.required_permissions:
            return True

        user = request.user

        if not user.is_authenticated:
            return False

        # Check if the user has a config with a role
        if not hasattr(user, "config") or not user.config.role:
            return False

        # Check for the specific permission or the wildcard permissions
        return user.config.role.permissions.filter(
            value__in=self.required_permissions
        ).exists()


class LogisticPermission(HasPermission):
    base_permission = ""

    def get_permissions(self, action):
        if self.base_permission:
            return [
                f"logistic.{self.base_permission}.{action}",
                "logistic.*",
                f"logistic.{self.base_permission}.*",
            ]
        return []


class HasCreateCommodityPermission(LogisticPermission):
    def __init__(self):
        self.base_permission = "commodity"
        self.required_permissions = self.get_permissions("create")


class HasReadCommodityPermission(LogisticPermission):
    def __init__(self):
        self.base_permission = "commodity"
        self.required_permissions = self.get_permissions("read")


class HasUpdateCommodityPermission(LogisticPermission):
    def __init__(self):
        self.base_permission = "commodity"
        self.required_permissions = self.get_permissions("update")


class HasDeleteCommodityPermission(LogisticPermission):
    def __init__(self):
        self.base_permission = "commodity"
        self.required_permissions = self.get_permissions("delete")


class HasCreateWarehousePermission(LogisticPermission):
    def __init__(self):
        self.base_permission = "warehouse"
        self.required_permissions = self.get_permissions("create")


class HasReadWarehousePermission(LogisticPermission):
    def __init__(self):
        self.base_permission = "warehouse"
        self.required_permissions = self.get_permissions("read")


class HasUpdateWarehousePermission(LogisticPermission):
    def __init__(self):
        self.base_permission = "warehouse"
        self.required_permissions = self.get_permissions("update")


class HasDeleteWarehousePermission(LogisticPermission):
    def __init__(self):
        self.base_permission = "warehouse"
        self.required_permissions = self.get_permissions("delete")


class HasCreateGoodHazardClassPermission(LogisticPermission):
    def __init__(self):
        self.base_permission = "good_hazard_class"
        self.required_permissions = self.get_permissions("create")


class HasReadGoodHazardClassPermission(LogisticPermission):
    def __init__(self):
        self.base_permission = "good_hazard_class"
        self.required_permissions = self.get_permissions("read")


class HasUpdateGoodHazardClassPermission(LogisticPermission):
    def __init__(self):
        self.base_permission = "good_hazard_class"
        self.required_permissions = self.get_permissions("update")


class HasDeleteGoodHazardClassPermission(LogisticPermission):
    def __init__(self):
        self.base_permission = "good_hazard_class"
        self.required_permissions = self.get_permissions("delete")


class HasCreateStorageConditionPermission(LogisticPermission):
    def __init__(self):
        self.base_permission = "storage_condition"
        self.required_permissions = self.get_permissions("create")


class HasReadStorageConditionPermission(LogisticPermission):
    def __init__(self):
        self.base_permission = "storage_condition"
        self.required_permissions = self.get_permissions("read")


class HasUpdateStorageConditionPermission(LogisticPermission):
    def __init__(self):
        self.base_permission = "storage_condition"
        self.required_permissions = self.get_permissions("update")


class HasDeleteStorageConditionPermission(LogisticPermission):
    def __init__(self):
        self.base_permission = "storage_condition"
        self.required_permissions = self.get_permissions("delete")
