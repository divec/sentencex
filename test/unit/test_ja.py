import pytest

from sentencex import segment

# ruff: noqa: E501
tests = [
    ("これはペンです。それはマーカーです。", ["これはペンです。", "それはマーカーです。"]),
    ("それは何ですか？ペンですか？", ["それは何ですか？", "ペンですか？"]),
    ("良かったね！すごい！", ["良かったね！", "すごい！"]),
    (
        "自民党税制調査会の幹部は、「引き下げ幅は３．２９％以上を目指すことになる」と指摘していて、今後、公明党と合意したうえで、３０日に決定する与党税制改正大綱に盛り込むことにしています。２％台後半を目指すとする方向で最終調整に入りました。",
        [
            "自民党税制調査会の幹部は、「引き下げ幅は３．２９％以上を目指すことになる」と指摘していて、今後、公明党と合意したうえで、３０日に決定する与党税制改正大綱に盛り込むことにしています。",
            "２％台後半を目指すとする方向で最終調整に入りました。",
        ],
    ),
    (
        "アンディ・ガトマンズ（英: Andi Gutmans、ヘブライ語: אנדי גוטמנס‎）はスイスにルーツを持つイスラエル人プログラマで、PHPの開発とゼンド・テクノロジーズの創業者の1人として知られている[1]。ハイファにあるイスラエル工科大学出身で、1997年に友人のゼーブ・スラスキーと共にPHP 3を開発した。1999年、PHP 4の中核である Zend Engine を開発し、ゼンド・テクノロジーズを創業。その後PHPの発展に関与し続け、PHP 5開発にも参加している[2]。なおZendという名称は、ガトマンズとスラスキーの名前（ZeevとAndi）を組み合わせたかばん語である[3]。 ハイファにあるイスラエル工科大学出身で、1997年に友人のゼーブ・スラスキーと共にPHP 3を開発した。1999年、PHP 4の中核である Zend Engine を開発し、ゼンド・テクノロジーズを創業。その後PHPの発展に関与し続け、PHP 5開発にも参加している[2]。なおZendという名称は、ガトマンズとスラスキーの名前（ZeevとAndi）を組み合わせたかばん語である[3]。",
        [
            "アンディ・ガトマンズ（英: Andi Gutmans、ヘブライ語: אנדי גוטמנס‎）はスイスにルーツを持つイスラエル人プログラマで、PHPの開発とゼンド・テクノロジーズの創業者の1人として知られている[1]。",
            "ハイファにあるイスラエル工科大学出身で、1997年に友人のゼーブ・スラスキーと共にPHP 3を開発した。1999年、PHP 4の中核である Zend Engine を開発し、ゼンド・テクノロジーズを創業。",
            "その後PHPの発展に関与し続け、PHP 5開発にも参加している[2]。",
            "なおZendという名称は、ガトマンズとスラスキーの名前（ZeevとAndi）を組み合わせたかばん語である[3]。",
            "ハイファにあるイスラエル工科大学出身で、1997年に友人のゼーブ・スラスキーと共にPHP 3を開発した。1999年、PHP 4の中核である Zend Engine を開発し、ゼンド・テクノロジーズを創業。",
            "その後PHPの発展に関与し続け、PHP 5開発にも参加している[2]。",
            "なおZendという名称は、ガトマンズとスラスキーの名前（ZeevとAndi）を組み合わせたかばん語である[3]。",
        ],
    ),
    (
        "ハイファにあるイスラエル工科大学出身で、1997年に友人のゼーブ・スラスキーと共にPHP 3を開発した。1999年、PHP 4の中核である Zend Engine を開発し、ゼンド・テクノロジーズを創業。その後PHPの発展に関与し続け、PHP 5開発にも参加している。なおZendという名称は、ガトマンズとスラスキーの名前（ZeevとAndi）を組み合わせたかばん語である。ハイファにあるイスラエル工科大学出身で、1997年に友人のゼーブ・スラスキーと共にPHP 3を開発した。1999年、PHP 4の中核である Zend Engine を開発し、ゼンド・テクノロジーズを創業。その後PHPの発展に関与し続け、PHP 5 開発にも参加している。なおZendという名称は、ガトマンズとスラスキーの名前（ZeevとAndi）を組み合わせたかばん語である。",
        [
            "ハイファにあるイスラエル工科大学出身で、1997年に友人のゼーブ・スラスキーと共にPHP 3を開発した。1999年、PHP 4の中核である Zend Engine を開発し、ゼンド・テクノロジーズを創業。",
            "その後PHPの発展に関与し続け、PHP 5開発にも参加している。",
            "なおZendという名称は、ガトマンズとスラスキーの名前（ZeevとAndi）を組み合わせたかばん語である。",
            "ハイファにあるイスラエル工科大学出身で、1997年に友人のゼーブ・スラスキーと共にPHP 3を開発した。1999年、PHP 4の中核である Zend Engine を開発し、ゼンド・テクノロジーズを創業。",
            "その後PHPの発展に関与し続け、PHP 5 開発にも参加している。",
            "なおZendという名称は、ガトマンズとスラスキーの名前（ZeevとAndi）を組み合わせたかばん語である。",
        ],
    ),
]


@pytest.mark.parametrize("text,expected_sents", tests)
def test_segment(text, expected_sents):
    assert list(segment("ja", text)) == expected_sents
