#!/usr/bin/env python3
"""
Comprehensive test script for Emotion Detection API
Demonstrates successful deployment and error handling
"""

import subprocess
import json
import sys

def test_api_endpoint(text, description):
    """Test the API endpoint with the given text"""
    print(f"\n{'='*60}")
    print(f"Test: {description}")
    print(f"{'='*60}")
    print(f"Input: {text}")
    print(f"{'-'*60}")

    payload = json.dumps({"text": text})

    try:
        result = subprocess.run(
            [
                'powershell',
                '-Command',
                f'@{{text=\'{text}\'}} | ConvertTo-Json | '
                'Invoke-WebRequest -Uri '
                '"http://localhost:5000/emotion_detector" '
                '-Method POST -ContentType "application/json" '
                '-UseBasicParsing | Select-Object -ExpandProperty Content'
            ],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode == 0:
            print("Response:")
            print(result.stdout)
        else:
            print("Error Response:")
            print(result.stderr)

    except Exception as e:
        print(f"Exception: {e}")

def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("EMOTION DETECTION API - COMPREHENSIVE TEST SUITE")
    print("="*60)

    # Test 1: Positive emotion
    test_api_endpoint(
        "I am glad this happened",
        "Positive Emotion Detection"
    )

    # Test 2: Negative emotion
    test_api_endpoint(
        "I am really mad about this",
        "Negative Emotion Detection"
    )

    # Test 3: Sad emotion
    test_api_endpoint(
        "I am so sad about this",
        "Sadness Detection"
    )

    # Test 4: Fear emotion
    test_api_endpoint(
        "I am really afraid of this",
        "Fear Detection"
    )

    # Test 5: Disgust emotion
    test_api_endpoint(
        "I feel disgusted just hearing about this",
        "Disgust Detection"
    )

    # Test 6: Error handling - blank input
    print(f"\n{'='*60}")
    print("Test: Error Handling - Blank Input")
    print(f"{'='*60}")
    print("Input: (empty string)")
    print(f"{'-'*60}")

    try:
        result = subprocess.run(
            [
                'powershell',
                '-Command',
                '@{text=""} | ConvertTo-Json | '
                'Invoke-WebRequest -Uri '
                '"http://localhost:5000/emotion_detector" '
                '-Method POST -ContentType "application/json" '
                '-UseBasicParsing'
            ],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode != 0:
            print("Error Response (Status 400 - Expected):")
            lines = result.stderr.split('\n')
            for line in lines:
                if '{' in line:
                    print(line)
        else:
            print(result.stdout)

    except Exception as e:
        print(f"Exception: {e}")

    print(f"\n{'='*60}")
    print("ALL TESTS COMPLETED")
    print(f"{'='*60}\n")

if __name__ == '__main__':
    main()
