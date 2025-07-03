from ninja import Router

router = Router()

@router.get("/hello")
def hello(request, name="world !"):
    return f"Hello {name}"

@router.get("/math")
def math(request, a: int, b: int):
    return {"add": a + b, "multiply": a * b}