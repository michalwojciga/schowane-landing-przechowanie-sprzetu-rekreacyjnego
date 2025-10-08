from __future__ import annotations


def test_landing_route_returns_success(client):
    response = client.get("/landing")

    assert response.status_code == 200

    html = response.data.decode("utf-8")
    assert "Schowane.pl" in html
    assert "Jak to działa" in html
    assert "Zarezerwuj teraz" in html
    assert "Zaufali nam właściciele sprzętu i operatorzy marin" in html
    assert "Stała ochrona 24/7" in html
    assert "Przekazujesz sprzęt, my zajmujemy się resztą" in html
    assert "Rezerwujesz i umawiasz odbiór" in html
    assert "Elastyczne pakiety dopasowane do Twojego sprzętu" in html
    assert "Mały sprzęt" in html
    assert "Opinie naszych klientów" in html
    assert "Najczęściej zadawane pytania" in html
    assert "Gotowy odzyskać przestrzeń i spokój?" in html
