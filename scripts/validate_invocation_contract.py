#!/usr/bin/env python3
import json
import sys
from pathlib import Path

REQUIRED = [
    'task',
    'selected_persona_mode',
    'selected_personas',
    'expected_output_shape',
]
VALID_MODES = {'single', 'dual', 'panel'}


def validate_item(item, idx):
    errors = []
    for key in REQUIRED:
        if key not in item:
            errors.append(f'item {idx}: missing required field `{key}`')
    mode = item.get('selected_persona_mode')
    personas = item.get('selected_personas')
    if mode is not None and mode not in VALID_MODES:
        errors.append(f'item {idx}: invalid mode `{mode}`')
    if personas is not None and not isinstance(personas, list):
        errors.append(f'item {idx}: `selected_personas` must be a list')
    if isinstance(personas, list):
        expected_count = {'single': 1, 'dual': 2, 'panel': 3}.get(mode)
        if expected_count and len(personas) != expected_count:
            errors.append(
                f'item {idx}: mode `{mode}` expects {expected_count} persona(s), got {len(personas)}'
            )
    return errors


def main():
    if len(sys.argv) != 2:
        print('usage: validate_invocation_contract.py <json-file>')
        return 2
    path = Path(sys.argv[1])
    data = json.loads(path.read_text())
    if not isinstance(data, list):
        print('top-level JSON must be a list')
        return 2
    errors = []
    for i, item in enumerate(data, 1):
        if not isinstance(item, dict):
            errors.append(f'item {i}: must be an object')
            continue
        errors.extend(validate_item(item, i))
    if errors:
        print('INVALID')
        for err in errors:
            print(f'- {err}')
        return 1
    print(f'VALID: {len(data)} invocation example(s) passed')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
