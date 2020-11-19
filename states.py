from aiogram.utils.helper import Helper, HelperMode, ListItem
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.filters.state import StatesGroup, State

class TestStates(Helper):
    mode = HelperMode.snake_case

    TEST_STATE_0 = ListItem()
    # TEST_STATE_1 = ListItem()
    # TEST_STATE_2 = ListItem()
    # TEST_STATE_3 = ListItem()
    # TEST_STATE_4 = ListItem()
    # TEST_STATE_5 = ListItem()

    TEST_STATE_0 = '0'
    TEST_STATE_1 = '1'
    TEST_STATE_2 = '2'

# dp = Dispatcher(bot, storage=MemoryStorage())
# dp.middleware.setup(LoggingMiddleware())