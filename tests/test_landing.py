from __future__ import annotations


def test_landing_route_returns_success(client):
    response = client.get("/landing")

    assert response.status_code == 200
    assert b"Schowane.pl" in response.data
