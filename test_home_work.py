import pytest
from homeWorkT3Class import BattleSimulation, ImportJson, Ship, Team
import json

class TestShip:
    def test_ship_import(self):
        ship = Ship(power=10.0,armor=20.0, shipName="TestShip")
        assert ship.armor == 20.0
        assert ship.power == 10.0
        assert ship.shipName == "TestShip"
    
    def test_get_hit(self):
        ship = Ship(power=10.0,armor=20.0, shipName="TestShip")
        ship.getHit(10.0)
        assert ship.armor == 10.0
        assert ship.isDrowning is False


    def test_get_hit_and_drown(self):
        ship =Ship(power=10.0,armor=20.0, shipName="TestShip")
        ship.getHit(100.0)
        assert ship.isDrowning is True

    def test_get_hit_and_drown_equal_armor(self):
        ship =Ship(power=10.0,armor=20.0, shipName="TestShip")
        ship.getHit(20)
        assert ship.isDrowning is True
        
        
class TestTeam:
    @pytest.fixture
    def sample_team(self):
        return [{"name":"TestName","armor":20,"hit":10}]
    
    def test_team_init(self, sample_team):
        team = Team(setTeam=sample_team)
        team.setShips()
        assert team._army is not None
        assert len(team._army) == 1
        
    def test_team_set_kill(self,sample_team):
        team = Team(setTeam=sample_team)
        team.setShips()
        team._army[0].isKilled = True
        team.teamCheckByAliveAndDrowning()
        assert len(team._army) == 0


@pytest.fixture
def valid_config_file(tmp_path):
    config = {
        "team1": [{"name": "blue", "armor": 40, "hit": 20}],
        "team2": [{"name": "red", "armor": 25, "hit": 10}]
    }
    file = tmp_path / "valid.json"
    file.write_text(json.dumps(config))
    return file

class TestBattleSimulation:
    @pytest.fixture
    def battle(self, valid_config_file):
        ij = ImportJson(valid_config_file)
        team1 = Team(ij.getTeam(1))
        team1.setShips()
        team2 = Team(ij.getTeam(2))
        team2.setShips()
        return BattleSimulation(team1, team2)

    def test_victory_conditions(self, battle):
        assert not battle.checkForVictory()
        battle.oneTeam._army.clear()
        assert battle.checkForVictory()
        
class TestImportJson:
    def test_valid_file_import(self, valid_config_file):
        imp = ImportJson(valid_config_file)
        assert len(imp.keyList) == 2
        assert imp.getTeam(1) == [{"name": "blue", "armor": 40, "hit": 20}]

    def test_invalid_team_number(self, valid_config_file):
        imp = ImportJson(valid_config_file)
        with pytest.raises(IndexError):
            imp.getTeam(3)