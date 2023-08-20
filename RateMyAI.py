import pandas as pd
import argparse
import textwrap
from colorama import Fore, Style, init

init(autoreset=True)  # Initialize colorama

# Load CSV data into a Pandas DataFrame (replace with your data)
try:
    prompts_df = pd.read_csv('prompts.csv')
except FileNotFoundError:
    prompts_df = pd.DataFrame()

selected_category = None
selected_prompts = []

def create_combined_prompt(prompt_ids):
    selected_prompts = prompts_df[prompts_df['ID'].isin(prompt_ids)]
    composite_prompt = '\n'.join(selected_prompts['prompt'])
    return composite_prompt

def display_main_menu():
    print(Fore.CYAN + r"````````````````````````````````````````")
    print(Fore.CYAN + r" /\_/\ ")
    print(Fore.CYAN + r"( o.o )    Welcome to RateMyAI - AI-Prompt Composer")
    print(Fore.CYAN + r" >^< ")
    print(Fore.CYAN + "milosilo.com")
    print(Fore.CYAN + r"````````````````````````````````````````" + Style.RESET_ALL)
    print(Fore.MAGENTA + "\nUsage Instructions:\n" + Style.RESET_ALL)
    print(Fore.YELLOW + "Available Categories:")
    categories = prompts_df['category'].unique()
    for index, category in enumerate(categories):
        print(f"{index + 1}. {category}")
    print(Style.RESET_ALL)

def main():
    global selected_category  # Add this line

    parser = argparse.ArgumentParser(description="Generate custom composite prompts for AI rating systems.")
    parser.add_argument('--cli', action='store_true', help="Run as a CLI prompt app.")
    parser.add_argument('--api', nargs='+', type=int, help="Generate combined prompt using prompt ID numbers (space-separated).")

    args = parser.parse_args()

    if args.cli:
        while True:
            display_main_menu()

            if selected_category is not None:
                print(Fore.YELLOW + f"\nSelected Category: {selected_category}\n" + Style.RESET_ALL)
                print(Fore.YELLOW + "Available Prompts:\n" + Style.RESET_ALL)
                available_prompts = prompts_df[prompts_df['category'] == selected_category]
                for index, prompt in available_prompts.iterrows():
                    print(f"{Fore.CYAN}{prompt['ID']}. {prompt['description']}{Style.RESET_ALL}")
                print()

            if selected_prompts:
                print(Fore.YELLOW + "Selected Prompts:" + Style.RESET_ALL)
                for prompt_id in selected_prompts:
                    prompt = prompts_df[prompts_df['ID'] == prompt_id].iloc[0]
                    print(f"{Fore.MAGENTA}Prompt ID: {prompt['ID']}, Description: {prompt['description']}{Style.RESET_ALL}")
                    print(textwrap.fill(prompt['prompt'], width=80))
                    print()

            print(Fore.GREEN + "help: Display usage instructions")
            print("exit: Exit the app")
            print("back: Go back to the main menu")
            print("show: Show selected prompts")
            print("combine: Combine prompts")

            user_input = input("Enter a command or selection: ")
            if user_input == "help":
                continue
            elif user_input == "exit":
                break
            elif user_input == "back":
                selected_category = None
                continue
            elif user_input == "show":
                continue
            elif user_input == "combine":
                combined_prompt = create_combined_prompt(selected_prompts)
                print(Fore.GREEN + "\nCombined Prompt:")
                print(combined_prompt)
                print(Style.RESET_ALL)
                break
            elif user_input.isdigit():
                selection = int(user_input)
                if selected_category is None:
                    categories = prompts_df['category'].unique()
                    if selection > 0 and selection <= len(categories):
                        selected_category = categories[selection - 1]
                else:
                    available_prompts = prompts_df[prompts_df['category'] == selected_category]
                    prompt_ids = available_prompts['ID'].tolist()
                    if selection in prompt_ids:
                        selected_prompts.append(selection)
            else:
                print("Invalid input. Please enter a valid command or selection.")
                continue

if __name__ == '__main__':
    main()
