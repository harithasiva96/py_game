import unittest
from hangman import image, dictionary, read_file, hang_man, start_game
from unittest.mock import patch, mock_open, call
from textwrap import dedent


class TestReadFile(unittest.TestCase):
    def test_read_file(self):
        
        mock_file_content = "reddit\nquora\ngoogle\n"
        expected_output = ['reddit', 'quora', 'google']

        with patch('builtins.open', mock_open(read_data=mock_file_content)):
            result = read_file()
            self.assertEqual(result, expected_output)

    def test_read_empty_file(self):
        # Mock content of an empty file
        mock_file_content = ""
        expected_output = []

        with patch('builtins.open', mock_open(read_data=mock_file_content)):
            result = read_file()
            self.assertEqual(result, expected_output)


class TestDict(unittest.TestCase):
    @patch('hangman.randint')
    def test_dictionary1(self,mock_randint):
        list_dict = ['PYTHON','FLASK','DJANGO','MYSQL','JAVA']  
        mock_randint.return_value = 4
        result = dictionary(list_dict)
        self.assertEqual(result, 'JAVA')

        
class TestImage(unittest.TestCase):
    
    def test_chance6(self):
        
        with patch('builtins.print') as mock_print:
            image(6)
        self.assertIn("""
                _______
                |      |
                |      
                |   
                |         """,mock_print.call_args.args[0])

    def test_chance1(self):
        with patch('builtins.print') as mock_print:
            image(1)
        self.assertIn("""
                _______
                |      |
                |      0
                |     /|\\
                |     /    """,mock_print.call_args.args[0])

   
    def test_chance_invalid(self):
        with patch('builtins.print') as mock_print:
            image(8)
        self.assertEqual("Something went wrong",mock_print.call_args.args[0])

class TestHangman(unittest.TestCase):

    @patch('hangman.read_file', return_value = None)
    @patch('hangman.dictionary',return_value = "PYTHON")
    @patch('hangman.image')
    @patch('hangman.input',side_effect = ['P','Y','T','H','O','N']) 
    def test_correct_guess_true(self,mock_readfile,mock_dictionary,mock_image,mock_input):

        with patch('builtins.print') as mock_print:
            hang_man()

        self.assertIn('Congrats!',mock_print.call_args.args[0])
    

    @patch('hangman.read_file', return_value = None)
    @patch('hangman.dictionary',return_value = "HELLO")
    @patch('hangman.image')
    @patch('hangman.input',side_effect = ['H','E','L','L','O']) 
    def test_correct_guess_repeat(self,mock_readfile,mock_dictionary,mock_image,mock_input):

        with patch('builtins.print') as mock_print:
            hang_man()

        self.assertIn('Congrats!',mock_print.call_args.args[0])

    
    @patch('hangman.read_file', return_value = None)
    @patch('hangman.dictionary',return_value = "HELLO")
    @patch('hangman.image')
    @patch('hangman.input',side_effect = ['H','E','L','L','Q','S','T','R','Y','Z','A']) 
    def test_wrong_guess(self,mock_read_file,mock_dictionary,mock_image,mock_input):

        with patch('builtins.print') as mock_print:
            hang_man()

        self.assertIn('Sorry',mock_print.call_args.args[0])


    @patch('hangman.read_file', return_value = None)
    @patch('hangman.dictionary',return_value = "HELLO")
    @patch('hangman.image')
    @patch('hangman.input',side_effect = ['H','E','L','L','L','O']) 
    def test_repeat_letter_before_completion(self,mock_read_file,mock_dictionary,mock_image,mock_input):

        with patch('builtins.print') as mock_print:
            hang_man()

        self.assertTrue(any("This letter is already guessed. Try another one." in call.args[0] for call in mock_print.call_args_list))
        self.assertIn('Congrats!',mock_print.call_args.args[0])
        self.assertNotIn('Sorry',mock_print.call_args.args[0])



    @patch('hangman.read_file', return_value = None)
    @patch('hangman.dictionary',return_value = "PYTHON")
    @patch('hangman.image')
    @patch('hangman.input',side_effect = ['P','Y','4','T','H','O','N']) 
    def test_number_guess(self,mock_read_file,mock_dictionary,mock_image,mock_input):

        with patch('builtins.print') as mock_print:
            hang_man()

        self.assertTrue(any("Your guess is not valid." in call.args[0] for call in mock_print.call_args_list))
        self.assertIn('Congrats!',mock_print.call_args.args[0])
        self.assertNotIn('Sorry',mock_print.call_args.args[0])



class TestStartGame(unittest.TestCase):

    @patch('builtins.input', side_effect=['n'])
    @patch('builtins.print')
    def test_quit_game(self, mock_print, mock_input):
        with self.assertRaises(SystemExit):
            start_game()
        mock_print.assert_has_calls([
            call("Would you like to play a game? Y/N?"),
            call("Ok, hope to see you later!")
        ])

   

    @patch('builtins.input', side_effect=['y', 'ok'])
    @patch('builtins.print')
    def test_start_hangman_game(self, mock_print, mock_input):
        with patch('hangman.hang_man', return_value="hangman_game_started") as mock_hangman:
            result = start_game()
            self.assertEqual(result, "hangman_game_started")
            mock_print.assert_has_calls([
                call("Would you like to play a game? Y/N?"),
                call("Welcome to Hangman out!"),
                call(dedent("""
                    The game is between you and a goblin.
                    Goblin will give you a word which is masked.
                    You should guess the word by guessing one letter at a time.
                    You can make 7 mistakes. For every mistake you will be one step ahead of your death.
                    Finally after your 7th mistake you will be hanged by the goblin.
                    Goblin loves brilliant brains. If you win the game "The treasure" is yours! :-)
                    Do your level best!
                     """)),
                call("Press ok to continue")
            ])
            mock_hangman.assert_called_once()


if __name__ == "__main__":
    unittest.main()
