from typing import Optional

from pyokra.base import BaseAsyncAPIWrapper, BaseAPIWrapper
from pyokra.utils import Mode
from pyokra.wrappers.account import Account, AsyncAccount
from pyokra.wrappers.auth import Auth, AsyncAuth
from pyokra.wrappers.balance import Balance, AsyncBalance
from pyokra.wrappers.bank import Bank, AsyncBank
from pyokra.wrappers.customer import Customer, AsyncCustomer
from pyokra.wrappers.identity import Identity, AsyncIdentity
from pyokra.wrappers.income import Income, AsyncIncome
from pyokra.wrappers.payments import Payment, AsyncPayment
from pyokra.wrappers.report import Report, AsyncReport
from pyokra.wrappers.sandbox import Sandbox, AsyncSandbox
from pyokra.wrappers.spending_patterns import SpendingPattern, AsyncSpendingPattern
from pyokra.wrappers.transactions import Transaction, AsyncTransaction
from pyokra.wrappers.wallet import Wallet, AsyncWallet


class Okra(BaseAPIWrapper):
    def __init__(self, token: Optional[str] = None, mode: Mode = Mode.DEVELOPMENT):
        super().__init__(token, mode)
        self.accounts = Account(token, mode)
        self.auths = Auth(token, mode)
        self.balances = Balance(token, mode)
        self.banks = Bank(token, mode)
        self.customers = Customer(token, mode)
        self.identities = Identity(token, mode)
        self.incomes = Income(token, mode)
        self.payments = Payment(token, mode)
        self.reports = Report(token, mode)
        self.sandbox = Sandbox(token, mode)
        self.spending_patterns = SpendingPattern(token, mode)
        self.transactions = Transaction(token, mode)
        self.wallets = Wallet(token, mode)


class AsyncOkra(BaseAsyncAPIWrapper):
    def __init__(self, token: Optional[str] = None, mode: Mode = Mode.DEVELOPMENT):
        super().__init__(token, mode)
        self.accounts = AsyncAccount(token, mode)
        self.auths = AsyncAuth(token, mode)
        self.balances = AsyncBalance(token, mode)
        self.banks = AsyncBank(token, mode)
        self.customers = AsyncCustomer(token, mode)
        self.identities = AsyncIdentity(token, mode)
        self.incomes = AsyncIncome(token, mode)
        self.payments = AsyncPayment(token, mode)
        self.reports = AsyncReport(token, mode)
        self.sandbox = AsyncSandbox(token, mode)
        self.spending_patterns = AsyncSpendingPattern(token, mode)
        self.transactions = AsyncTransaction(token, mode)
        self.wallets = AsyncWallet(token, mode)
