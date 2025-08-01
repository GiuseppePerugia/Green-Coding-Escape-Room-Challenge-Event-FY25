## Template that can work without Import
def solve_password(do):
    all_chars = do.get_list_of_characters()

    # 2) Count how many times each actually appears
    char_counts = {}
    total_len = 0
    # For each character in the allowed list:
    #   - Use do.guess_character(char) to find out how many times it appears in the password
    #   - If the count is greater than zero:
    #       - Add it to a dictionary mapping the character to its count
    #       - Also keep a running total of how many characters are in the full password

    # How might you track how many times each character has been used so far?

    def dfs(prefix):
        # What condition tells you the password is complete?

        for ch, maxcnt in char_counts.items():
            if ...:  # Have we used this character too many times?
                new_pref = # What happens if you add this character to the current prefix?

                if ...: # How might you avoid wasting time? Try checking if the new prefix is still valid using do.guess_substring.
                    # Mark this character as used
                    result = dfs(new_pref)
                    if result is not None:
                        return result
                    ... # Backtrack: undo the character use
        return None

    password = dfs("")
    if password is None:
        raise RuntimeError("Failed to reconstruct password!")
    
    do.enter_password(password)
solve_password(do)