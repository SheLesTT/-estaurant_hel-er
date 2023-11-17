from fastapi import APIRouter


from src.main import app

router = APIRouter(
    prefix='/posts',
    tags=["Posts"]
)


@router.get("/")
def get_menu_items():
    pass

@router.get("/{id}")
def get_menu_item():
    pass

@router.post("/")
def create_menu_item():
    pass
