from src.stock import classify_tub


def test_classify_tub():
  # ARRANGE
    tub = {}
  #ACT
    result = classify_tub(tub)
    #ASSERT
    assert type(result) == dict