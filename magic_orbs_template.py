## Template that can work without Import

def solve_orbs(do):
    
    def count_number_of_orbs(do):
        orb_colors = do.get_orbs()
        count = # How might we work out the number of orbs from our available functions?
        return count

    def find_correct_position(do, current_position):
        color = # We need to find the colour at the given position
        correct_position = # We need to find the colour at the given position
        return correct_position

    def loop_and_swap(do):
        total_orbs = count_number_of_orbs(do)
        # Loop going over positions goes here
            correct_position = find_correct_position(do, position)
            # Do this if the position is not correct:
                do.swap_position(position, correct_position)

    loop_and_swap(do)

solve_orbs(do)