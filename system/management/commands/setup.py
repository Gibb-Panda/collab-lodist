from django.core.management.base import BaseCommand

from system.models import CustomPermission, Role


class Command(BaseCommand):
    help = "Set up initial permissions and roles"

    def handle(self, *args, **options):
        if CustomPermission.objects.exists():
            self.stdout.write(
                self.style.WARNING(
                    "Info: Roles and rights have already been created, so the setup command was skipped."
                )
            )
            return

        permissions = [
            "*",
            "system.*",
            "system.role.*",
            "system.role.create",
            "system.role.read",
            "system.role.update",
            "system.role.delete",
            "system.permission.*",
            "system.permission.create",
            "system.permission.read",
            "system.permission.update",
            "system.permission.delete",
            "logistic.*",
            "logistic.commodity.*",
            "logistic.commodity.create",
            "logistic.commodity.read",
            "logistic.commodity.update",
            "logistic.commodity.delete",
            "logistic.warehouse.*",
            "logistic.warehouse.create",
            "logistic.warehouse.read",
            "logistic.warehouse.update",
            "logistic.warehouse.delete",
            "logistic.good_hazard_class.*",
            "logistic.good_hazard_class.create",
            "logistic.good_hazard_class.read",
            "logistic.good_hazard_class.update",
            "logistic.good_hazard_class.delete",
            "logistic.storage_condition.*",
            "logistic.storage_condition.create",
            "logistic.storage_condition.read",
            "logistic.storage_condition.update",
            "logistic.storage_condition.delete",
            "disposition.*",
            "disposition.tour.*",
            "disposition.tour.create",
            "disposition.tour.read.other",
            "disposition.tour.read.assigned",
            "disposition.tour.update.other",
            "disposition.tour.update.assigned",
            "disposition.tour.delete",
            "disposition.vehicle.*",
            "disposition.vehicle.create",
            "disposition.vehicle.read",
            "disposition.vehicle.update",
            "disposition.vehicle.delete",
        ]

        permission_descriptions = {
            "*": "All rights",
            "system.*": "All rights in user management",
            "system.role.*": "All CRUD rights for roles",
            "system.role.create": "Can create roles",
            "system.role.read": "Can view all existing roles, including details",
            "system.role.update": "Can update roles",
            "system.role.delete": "Can delete roles",
            "system.permission.*": "All CRUD rights for permissions",
            "system.permission.create": "Can create permissions",
            "system.permission.read": "Can view all existing permissions, including details",
            "system.permission.update": "Can update permissions",
            "system.permission.delete": "Can delete permissions",
            "logistic.*": "All logistics-related rights",
            "logistic.commodity.*": "All CRUD rights for commodities",
            "logistic.commodity.create": "Can create commodities",
            "logistic.commodity.read": "Can view all commodities, including details",
            "logistic.commodity.update": "Can update commodities",
            "logistic.commodity.delete": "Can delete commodities",
            "logistic.warehouse.*": "All CRUD rights for warehouses",
            "logistic.warehouse.create": "Can create warehouses",
            "logistic.warehouse.read": "Can view all warehouses, including details",
            "logistic.warehouse.update": "Can update warehouses",
            "logistic.warehouse.delete": "Can delete warehouses",
            "logistic.good_hazard_class.*": "All CRUD rights for good hazard classes",
            "logistic.good_hazard_class.create": "Can create good hazard classes",
            "logistic.good_hazard_class.read": "Can view all good hazard classes, including details",
            "logistic.good_hazard_class.update": "Can update good hazard classes",
            "logistic.good_hazard_class.delete": "Can delete good hazard classes",
            "logistic.storage_condition.*": "All CRUD rights for storage conditions",
            "logistic.storage_condition.create": "Can create storage conditions",
            "logistic.storage_condition.read": "Can view all storage conditions, including details",
            "logistic.storage_condition.update": "Can update storage conditions",
            "logistic.storage_condition.delete": "Can delete storage conditions",
            "disposition.*": "All disposition-related rights",
            "disposition.tour.*": "All CRUD rights for tours",
            "disposition.tour.create": "Can create tours",
            "disposition.tour.read.other": "Can view all tours, including details",
            "disposition.tour.read.assigned": "Can view only assigned tours, including details",
            "disposition.tour.update.other": "Can update all tours",
            "disposition.tour.update.assigned": "Can update only assigned tours",
            "disposition.tour.delete": "Can delete tours",
            "disposition.vehicle.*": "All CRUD rights for vehicles",
            "disposition.vehicle.create": "Can create vehicles",
            "disposition.vehicle.read": "Can view all vehicles, including details",
            "disposition.vehicle.update": "Can update vehicles",
            "disposition.vehicle.delete": "Can delete vehicles",
        }

        created_permissions = {}
        for perm in permissions:
            created_permissions[perm] = CustomPermission.objects.create(
                value=perm, description=permission_descriptions[perm]
            )

        roles_permissions = {
            "Root": ["*"],
            "Administrator": ["system.*", "logistic.*", "disposition.*"],
            "Dispatcher": [
                "disposition.*",
                "logistic.commodity.update",
                "logistic.warehouse.update",
                "logistic.good_hazard_class.update",
                "logistic.storage_condition.update",
            ],
            "Logistician": ["logistic.commodity.*", "logistic.*"],
            "Vehicle Manager": [
                "disposition.vehicle.read",
                "disposition.vehicle.update",
            ],
            "Road Transport Specialist": [
                "disposition.tour.read.assigned",
                "disposition.tour.update.assigned",
            ],
        }
        self.stdout.write(self.style.SQL_FIELD(f""))

        self.stdout.write(
            self.style.SQL_FIELD(
                f"▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ ✦ DATABASE ✦ ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇"
            )
        )
        for role_name, role_perms in roles_permissions.items():
            role, created = Role.objects.get_or_create(name=role_name)
            if "*" in role_perms:
                role.permissions.set(CustomPermission.objects.all())
            else:
                for perm in role_perms:
                    role.permissions.add(created_permissions[perm])
            role.save()

            self.stdout.write(self.style.SQL_FIELD(f"▇"))
            self.stdout.write(self.style.SQL_FIELD(f"▇ {role_name}"))

            # Header for the permissions table
            self.stdout.write(
                self.style.SQL_FIELD(f"▇   {'Permission':<40} {'Description'}")
            )
            self.stdout.write(self.style.SQL_FIELD(f"▇   {'-'*40} {'-'*40}"))

            # Display each permission in a tabular format
            for perm in role.permissions.all():
                self.stdout.write(
                    self.style.SQL_FIELD(f"▇   {perm.value:<40} {perm.description}")
                )

        self.stdout.write(self.style.SQL_FIELD(f"▇"))
        self.stdout.write(
            self.style.SQL_FIELD(
                f"▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ ✦ DATABASE ✦ ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇"
            )
        )
        self.stdout.write(self.style.SQL_FIELD(f""))

        self.stdout.write(
            self.style.SUCCESS(
                "✓ SUCCESS: Successfully configured roles and rights in the database for Collab Lodist"
            )
        )
