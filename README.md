# RateMyAI

![RateMyAI](https://milosilo.com/wp-content/uploads/2023/08/Screenshot-2023-08-19-212324.png)

Prompt Engineering Tool for AI Models with cli prompt or api usage

Full Research Write-up:

https://milosilo.com/hacking/ai-cognitive-behavioral-analysis-for-prompt-engineering-using-ratemyai/
## RateMyAI Prompt Composer User Guide


Welcome to the RateMyAI Prompt Composer, a versatile tool designed to help you create custom composite prompts for AI rating systems. This guide will take you through using the tool's CLI mode and API mode, highlighting its potential for security testing and its integration with AI models.

### Table of Contents

1. [Introduction](#introduction)
2. [Dependencies](#dependencies)
3. [CLI Mode](#cli-mode)
    - [Usage Instructions](#usage-instructions)
    - [Selecting a Category](#selecting-a-category)
    - [Adding Prompts to the Selection](#adding-prompts-to-the-selection)
    - [Viewing Selected Prompts](#viewing-selected-prompts)
    - [Combining Selected Prompts](#combining-selected-prompts)
4. [API Mode](#api-mode)
    - [Usage Instructions](#usage-instructions-1)
    - [Generating Combined Prompts](#generating-combined-prompts)
5. [Benefits for Security Testing](#benefits-for-security-testing)
6. [Integration with AI Models](#integration-with-ai-models)
7. [Prompts.csv File](#prompts-csv-file)
8. [Using the RateMyAI Prompt Composer](#using-the-ratemyai-prompt-composer)

### Introduction

The RateMyAI Prompt Composer empowers you to create custom composite prompts for AI rating systems, enhancing your control over AI-generated responses. This guide covers both CLI mode for interactive use and API mode for scripting.

### Dependencies

Before using the RateMyAI Prompt Composer, ensure you have the following dependencies installed:

- Python 3.x
- pandas library
- colorama library (optional for enhanced CLI output)

You can install the required libraries using the following commands:

```bash
pip install pandas colorama
```

### CLI Mode

#### Usage Instructions

To launch the tool in CLI mode, navigate to the directory containing the script and run:

```bash
python RateMyAI.py --cli
```

#### Selecting a Category

Choose a category from the main menu by entering the corresponding number.

#### Adding Prompts to the Selection

Select prompts by entering their ID numbers, regardless of category.

#### Viewing Selected Prompts

Use the "show" command to view selected prompts, including descriptions.

#### Combining Selected Prompts

Generate a combined prompt by typing "combine." Exit with "exit."

### API Mode

#### Usage Instructions

For API mode, generate combined prompts using prompt ID numbers:

```bash
python RateMyAI.py --api prompt_id_1 prompt_id_2 prompt_id_3 ...
```

### Benefits for Security Testing

The RateMyAI Prompt Composer is an ideal tool for security testing AI systems. By generating prompts that instruct AI models to use specific settings or techniques, you can gain deeper insights into how the AI responds and assess its behavior in controlled scenarios. This can help identify vulnerabilities and potential risks.

### Integration with AI Models

The tool's ability to compose prompts is also integrated into AI models like ChatGPT. With the addition of a new user setting, prompts can be executed at the start of every conversation, allowing you to set the stage for interactions. This innovative feature is designed to make the conversation align with your intentions and provide clearer instructions to the AI model.

### Prompts.csv File

The `prompts.csv` file contains the available prompts organized by category, ID, name, and description. This file serves as the source of prompts that you can select and combine using the RateMyAI Prompt Composer. To add new prompts or modify existing ones, simply update the `prompts.csv` file with the desired information.

### Using the RateMyAI Prompt Composer

To use the RateMyAI Prompt Composer, follow these steps:

1. Launch the tool in CLI mode or API mode based on your requirements.
2. Navigate through the interactive menus to select prompts from different categories.
3. Add prompts to the selection by entering their ID numbers.
4. View selected prompts, descriptions, and the combined prompt when desired.
5. Experiment with combining different prompts to shape AI model responses.
6. Utilize the tool for security testing, research, automation, and more.

With its security testing potential and seamless integration with AI models, the RateMyAI Prompt Composer offers a powerful way to shape AI-generated responses and evaluate their behavior. By harnessing its capabilities, you can enhance the accuracy and reliability of AI interactions while uncovering potential areas for improvement. Happy composing and exploring!

---

Feel free to consult this guide whenever you use the RateMyAI Prompt Composer. It will help you navigate the tool's features, understand its benefits, and make the most out of your interactions with AI models.

For any further assistance or inquiries, don't hesitate to reach out to us at [milosilo.com](http://milosilo.com).

*(Note: The tool and guide are provided as
