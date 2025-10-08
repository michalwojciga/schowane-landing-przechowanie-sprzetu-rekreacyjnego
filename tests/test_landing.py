from __future__ import annotations


def test_landing_route_returns_success(client):
    response = client.get("/landing")

    assert response.status_code == 200

    html = response.data.decode("utf-8")
    assert "Schowane.pl" in html
    assert "Jak to działa" in html
    assert "Zarezerwuj teraz" in html
