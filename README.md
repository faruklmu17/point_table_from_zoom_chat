# Points Table Generator

This Python script reads a Zoom chat log file and generates a cumulative points table for each participant based on specific message patterns.

## Features

* Parses chat logs for messages in the format `"From <username> to Everyone:"`
* Excludes messages from `Faruk Hasan`
* Counts the number of qualifying messages per user
* Outputs a sorted table of users and their point totals

## Requirements

* Python 3.x

## Usage

1. Place your chat log file named `meeting_saved_new_chat.txt` in the same directory as the script.
2. Run the script:

   ```bash
   python3 points_table.py
   ```
3. View the output, for example:

   ```
   Cumulative Points Table:
   ------------------------------
   Alice: 5
   Bob: 3
   ```

## How It Works

1. **`create_points_table(text)`** function:

   * Splits the input text into lines.
   * Searches each line for the patterns `" From "` and `" to Everyone:"`.
   * Extracts the username between those markers, excluding `Faruk Hasan`.
   * Increments the user's count in a dictionary.
2. The script reads the entire contents of `meeting_saved_new_chat.txt`.
3. Calls `create_points_table` to build the points dictionary.
4. Prints the users and their point totals in descending order.

## File Structure

```
.
├── points_table.py               # Main script
├── meeting_saved_new_chat.txt    # Zoom chat log file
└── README.md                     # This documentation
```

## License

MIT License

Copyright (c) 2025 Faruk Hasan

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
