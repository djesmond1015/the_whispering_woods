# Documentation

This documentation is for the game developer. If you are a user, please refer to the [README.md](../README.md) file.

## Table of Contents

- [Documentation](#documentation)
  - [Table of Contents](#table-of-contents)
  - [Customize the game flow](#customize-the-game-flow)
    - [Data structure of a scene](#data-structure-of-a-scene)
    - [Explanation of the scene data structure](#explanation-of-the-scene-data-structure)
    - [Cases of the scene](#cases-of-the-scene)
    - [Configure scene based on the cases](#configure-scene-based-on-the-cases)

<br>

## Customize the game flow

### Data structure of a scene

```python
 {
        "name": "Path ahead blocked by ancient trees",
        "text": {
            SceneText.NARRATIVES: [
                "As you venture deeper into the grove, ancient trees materialize, forming an impenetrable barrier across your path. Their gnarled roots and twisted branches seem to converge, creating an enchantment that obstructs any attempt to move forward. The barrier is a testament to the grove's protective magic. The seeker must unravel the threads of nature's enchantment, proving their understanding of the delicate balance that sustains this magical sanctuary."
            ],
            SceneText.DIALOGUES: [
                "Ancient Guardian's Whispers: The ancient trees, guardians of the magical grove, seem to communicate through rustling leaves and creaking branches. \"Bearer of the vortex's touch, only those attuned to the essence of this realm may pass beyond this threshold.\""
            ],
            SceneText.CHOICES: [
                "Choose the path you want to continue: ",
                "[1] - Continue ahead",
                "[2] - Try to find a way out",
            ],
        },
        "choice": {
            "1": "Continue ahead",
            "2": "Try to find a way out",
        },
        "continue": (False, None),
    }
```

<br>

### Explanation of the scene data structure

1. `name`: The name of the scene. This is used to identify the scene.
2. `text`: The text of the scene. All text will be displayed in the terminal. This is a dictionary that contains the following keys:
   1. `SceneText.NARRATIVES`: The narrative text of the scene. This is a list of strings.
   2. `SceneText.DIALOGUES`: The dialogue text of the scene. This is a list of strings.
   3. `SceneText.CHOICES`: The choices text of the scene. This is a list of strings.
3. `choice`: The choices of the scene following the format of `{"choice_number": "choice_text"}`, where `choice_number` is used as the key to identify the choice and `choice_text` is the text of the choice. For instance, based on the above example, the user will be directed to `Continue ahead` scene if the user chooses `1` and `Try to find a way out` scene if the user chooses `2`.
4. `continue`: A tuple of `(isContinue, next_scene_name)`. `isContinue` is a boolean value that determine the behavior of the game.`next_scene_name` is the name of the next scene. It should be the same as the `name` of the next scene.

- If `isContinue` is `False`, the game is non-linear, allowing the user to choose the next scene.
- If `isContinue` is `True`, the game is linear, either the game will continue to the next scene or the game will end.

```python
(True, "next_scene_name") # No choices scene
(False, None) # End scene or choices scene
```

<br>

### Cases of the scene

There are 3 cases of the scene:

1. No choices scene: The scene has no choices and the game will continue to the next scene when the user presses any key.
2. Choices: The scene has choices and the game will continue to the next scene based on the user's choice. (Choices)
3. End: The scene has no choices and the game will end when the user presses any key.

<br>

### Configure scene based on the cases

1. No choices scene: The `SceneText.CHOICES` and `choice` dictionary should be empty, and the `continue` tuple should be `(True, None)`.

```python
{
    "name": # The name of the scene,
    "text": {
        SceneText.NARRATIVES: [
            # Narratives text
        ],
        SceneText.DIALOGUES: [
            # Dialogues text

        ],
        SceneText.CHOICES: [],
    },
    "choice": {},
    "continue": (True, None),
}
```

<br>

2. Choices scene: The `SceneText.CHOICES` and `choice` dictionary should be filled with the same number, and the `continue` tuple should be `(True, None)`.

```python
{
    "name": # The name of the scene,
    "text": {
        SceneText.NARRATIVES: [
            # Narratives text
        ],
        SceneText.DIALOGUES: [
            # Dialogues text
        ],
        SceneText.CHOICES: [
            # Note: number of scene.CHOICES == number of choice
            "[1] - Choice 1",
            "[2] - Choice 2",
            "[N] - Choice N",
        ],
    },
    "choice": {
        # Note: number of choice == number of scene.CHOICES
        "1": "Choice 1",
        "2": "Choice 2",
        "N": "Choice N",
    },
    "continue": (True, None),
}
```

<br>

3. End scene: The `SceneText.CHOICES` and `choice` dictionary should be empty, and the `continue` tuple should be `(False, None)`.

```python
{
    "name": # The name of the scene,
    "text": {
        SceneText.NARRATIVES: [
            # Narratives text
        ],
        SceneText.DIALOGUES: [
            # Dialogues text
        ],
        SceneText.CHOICES: [],
    },
    "choice": {},
    "continue": (False, None),
}
```

<br>
