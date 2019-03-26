from src.menu import Menu, MSG_REQUIRE_MODE, MSG_REQUIRE_MODE_IS_NUMBER, MSG_REQUIRE_MODE_VALID_RANGE

if __name__ == '__main__':
    menu = Menu()
    menu.print()
    while True:
        try:
            choose = int(input(MSG_REQUIRE_MODE))
            if choose == 1:
                menu.new_user()
            elif choose == 2:
                menu.validate_password()
            elif choose == 3:
                menu.login()
            elif choose == 4:
                menu.change_password()
            elif choose == 5:
                break
            else:
                print(MSG_REQUIRE_MODE_VALID_RANGE)
        except ValueError:
            print(MSG_REQUIRE_MODE_IS_NUMBER)
            continue
        except Exception:
            print('Something error')
            continue
        menu.print_dash()