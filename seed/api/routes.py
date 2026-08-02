from fastapi import APIRouter

from seed.api.service import ReviewService

router = APIRouter(prefix="/reviews")


@router.get("/")
def get_reviews():

    return ReviewService.get_reviews()