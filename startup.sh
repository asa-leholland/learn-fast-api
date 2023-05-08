#!/bin/bash

# # Create project directories
# mkdir -p src/domain/{models,repositories,services}
# mkdir -p src/interfaces/web/controllers
# mkdir -p src/interfaces/api/endpoints
# mkdir tests

# # Create project files
# touch src/__init__.py
# touch src/domain/__init__.py
# touch src/domain/models/__init__.py
# touch src/domain/repositories/__init__.py
# touch src/domain/services/__init__.py
# touch src/interfaces/__init__.py
# touch src/interfaces/web/__init__.py
# touch src/interfaces/api/__init__.py
# touch src/interfaces/api/endpoints/__init__.py
# touch tests/__init__.py

# # Add content to project files
# echo "from fastapi import FastAPI" >> src/interfaces/api/__init__.py
# echo "app = FastAPI()" >> src/interfaces/api/__init__.py

# echo "from .endpoints import router" >> src/interfaces/api/__init__.py
# echo "app.include_router(router)" >> src/interfaces/api/__init__.py

# echo "from fastapi import APIRouter" >> src/interfaces/api/endpoints/__init__.py
# echo "router = APIRouter()" >> src/interfaces/api/endpoints/__init__.py

# echo "from fastapi import FastAPI" >> src/interfaces/web/controllers/__init__.py
# echo "from fastapi.responses import HTMLResponse" >> src/interfaces/web/controllers/__init__.py
# echo "app = FastAPI()" >> src/interfaces/web/controllers/__init__.py

# echo "from . import app" >> tests/__init__.py

# echo "print('Project structure created successfully!')" # Optional message

# #!/bin/bash

# # Create project directories
# mkdir -p src/application/use_cases
# mkdir -p src/domain/factories
# mkdir -p src/domain/value_objects
# mkdir -p src/infrastructure/services
# mkdir -p tests/application/use_cases
# mkdir -p tests/domain/factories
# mkdir -p tests/infrastructure/services

# # Create project files
# touch src/application/__init__.py
# touch src/application/use_cases/__init__.py
# touch src/application/use_cases/create_work_order.py
# touch src/domain/__init__.py
# touch src/domain/factories/__init__.py
# touch src/domain/factories/work_order_factory.py
# touch src/domain/models.py
# touch src/domain/value_objects/__init__.py
# touch src/domain/value_objects/routing.py
# touch src/infrastructure/__init__.py
# touch src/infrastructure/services/__init__.py
# touch src/infrastructure/services/item_card_service.py
# touch tests/application/__init__.py
# touch tests/domain/__init__.py
# touch tests/domain/factories/__init__.py
# touch tests/domain/factories/test_work_order_factory.py
# touch tests/domain/value_objects/__init__.py
# touch tests/domain/value_objects/test_routing.py
# touch tests/infrastructure/__init__.py
# touch tests/infrastructure/services/__init__.py
# touch tests/infrastructure/services/test_item_card_service.py

# # Add content to project files
# echo "from dataclasses import dataclass" >> src/domain/models.py

# echo "from .value_objects import Routing" >> src/domain/factories/work_order_factory.py
# echo "from ..models import WorkOrder" >> src/domain/factories/work_order_factory.py
# echo "from ..value_objects import Routing" >> src/domain/factories/work_order_factory.py
# echo "@dataclass" >> src/domain/factories/work_order_factory.py
# echo "class WorkOrderFactory:" >> src/domain/factories/work_order_factory.py
# echo "    @staticmethod" >> src/domain/factories/work_order_factory.py
# echo "    def create_work_order(routing: Routing, quantity: int) -> WorkOrder:" >> src/domain/factories/work_order_factory.py
# echo "        # Implementation goes here" >> src/domain/factories/work_order_factory.py

# echo "from typing import List" >> src/infrastructure/services/item_card_service.py
# echo "class ItemCardService:" >> src/infrastructure/services/item_card_service.py
# echo "    @staticmethod" >> src/infrastructure/services/item_card_service.py
# echo "    def get_available_work_order_options() -> List[str]:" >> src/infrastructure/services/item_card_service.py
# echo "        # Implementation goes here" >> src/infrastructure/services/item_card_service.py

# echo "from fastapi import APIRouter" >> src/interfaces/api/endpoints/__init__.py
# echo "from ...application.use_cases.create_work_order import create_work_order" >> src/interfaces/api/endpoints/__init__.py
# echo "router = APIRouter()" >> src/interfaces/api/endpoints/__init__.py
# echo "@router.post('/work-orders')" >> src/interfaces/api/endpoints/__init__.py
# echo "async def create_work_order_endpoint(routing: str, quantity: int):" >> src/interfaces/api/endpoints/__init__.py
# echo "    result = create_work_order(routing, quantity)" >> src/interfaces/api/endpoints/__init__.py
# echo "    # Return response goes here" >> src/interfaces/api/endpoints/__init__.py

# echo "from ...domain.factories.work_order_factory import WorkOrderFactory" >> tests/domain/factories/test_work_order_factory.py
# echo "from ...value_objects.routing import Routing" >> tests/domain


# mkdir -p myapp/controllers
# mkdir -p myapp/models
# mkdir -p myapp/views/home
# mkdir -p myapp/views/users
# mkdir -p myapp/tests/controllers
# mkdir -p myapp/tests/models


# # #!/bin/bash

# # Create the app directory structure
# mkdir myapp
# cd myapp
# mkdir app
# mkdir tests

# # Create the app package directory structure
# cd app
# mkdir models
# mkdir controllers
# mkdir views

# # Create the views package directory structure
# cd views
# mkdir home
# mkdir users

# # Create the tests package directory structure
# cd ../../tests
# mkdir test_controllers
# mkdir test_models



#!/bin/bash

# Presentation Layer
mkdir -p PresentationLayer/WorkOrderView
mkdir -p PresentationLayer/PickListView

# Application Layer
mkdir -p ApplicationLayer/WorkOrderController
mkdir -p ApplicationLayer/ItemCardController

# Domain Layer
mkdir -p DomainLayer/WorkOrderService
mkdir -p DomainLayer/ItemCardService

# Data Layer
mkdir -p DataLayer/WorkOrderRepository
mkdir -p DataLayer/ItemCardRepository
