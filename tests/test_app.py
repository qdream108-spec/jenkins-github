from app import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello from Jenkins + Python!" in captured.out
