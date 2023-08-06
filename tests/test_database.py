import psycopg2
import pytest

from src.database import DataBase
from src.config import config
from tests.test_employer import employer_fixture