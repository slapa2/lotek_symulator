from main import draw_six_numbers


def test_draw_numbers():

    for _ in range(500):
        draw_numbers = draw_six_numbers(list(range(1,50)))
        assert len(draw_numbers) == 6
        assert all([x >= 1 for x in draw_numbers])
        assert all([x <= 49 for x in draw_numbers])
