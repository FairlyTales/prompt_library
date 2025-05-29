import marimo

__generated_with = "0.13.14"
app = marimo.App(width="medium")


@app.cell
def _():
    import re  # For regex to extract placeholders

    import marimo as mo

    from src.marimo_notebook.modules import prompt_library_module
    return mo, prompt_library_module, re


@app.cell
def _(prompt_library_module):
    map_prompt_library: dict = prompt_library_module.pull_in_prompt_library()
    return (map_prompt_library,)


@app.cell
def _(map_prompt_library: dict, mo):
    prompt_keys = list(map_prompt_library.keys())
    prompt_dropdown = mo.ui.dropdown(
        options=prompt_keys,
        label="Select prompt",
    )
    return prompt_dropdown


@app.cell
def _(prompt_dropdown, mo):
    prompt_dropdown

    return prompt_dropdown

@app.cell
def _(map_prompt_library: dict, mo, prompt_dropdown):
    selected_prompt_name = None
    selected_prompt = None

    mo.stop(not prompt_dropdown.value, "")
    selected_prompt_name = prompt_dropdown.selected_key
    selected_prompt = map_prompt_library[selected_prompt_name]
    
    code_editor = mo.ui.code_editor(
                value=selected_prompt,
                language="xml",
                show_copy_button=True,
            )

    code_editor

    return code_editor, selected_prompt_name


@app.cell
def _(code_editor):
    edited_selected_prompt = code_editor.value
    return (edited_selected_prompt,)


@app.cell
def _(edited_selected_prompt, mo, re, selected_prompt_name):
    mo.stop(not selected_prompt_name or not edited_selected_prompt, "")

    # Extract placeholders from the prompt
    placeholders = re.findall(r"\{\{(.*?)\}\}", edited_selected_prompt)
    placeholders = list(set(placeholders))  # Remove duplicates
    placeholders = sorted(placeholders)

    # Create text areas for placeholders, using the placeholder text as the label
    placeholder_inputs = [
        mo.ui.text_area(label=ph, placeholder=f"Enter {ph}", full_width=True)
        for ph in placeholders
    ]

    # Create an array of placeholder inputs
    placeholder_array = mo.ui.array(
        placeholder_inputs,
        label="Enter values",
    )

    # Create a 'Proceed' button
    proceed_button = mo.ui.run_button(label="Confirm")

    # Display the placeholders and the 'Proceed' button in a vertical stack
    vstack = mo.vstack([placeholder_array, proceed_button])
    vstack
    return placeholder_array, placeholders, proceed_button


@app.cell
def _(mo, placeholder_array, placeholders, proceed_button):
    mo.stop(not placeholder_array.value or not len(placeholder_array.value), "")

    # Check if any values are missing
    if any(not value.strip() for value in placeholder_array.value):
        mo.stop(True)

    # Ensure the 'Confirm' button has been pressed
    mo.stop(
        not proceed_button.value,
        mo.md("**Press the 'Confirm' button.**"),
    )

    # Map the placeholder names to the values
    filled_values = dict(zip(placeholders, placeholder_array.value))
    return (filled_values,)


@app.cell
def _(edited_selected_prompt, filled_values):
    # Replace placeholders in the prompt
    final_prompt = edited_selected_prompt
    for key, value in filled_values.items():
        final_prompt = final_prompt.replace(f"{{{{{key}}}}}", value)

    # Create context_filled_prompt
    context_filled_prompt = final_prompt
    return (context_filled_prompt,)


@app.cell
def _(context_filled_prompt, mo):
    mo.ui.code_editor(
                value=context_filled_prompt,
                language="xml",
                show_copy_button=True
            )
    return


if __name__ == "__main__":
    app.run()
