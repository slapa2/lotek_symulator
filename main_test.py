from main import draw_six_numbers

def test_draw_numbers():

    for _ in range(500):
        # given
        # when
        drow_numbers = draw_six_numbers()
        #then
        assert len(drow_numbers) == 6
        assert all([x >= 1 for x in drow_numbers])
        assert all([x <= 49 for x in drow_numbers])
