from main import Component, ComponentType, InvestmentClass, Account, Portfolio, Allocation

def test_basic():
    bond = InvestmentClass('Bond')
    equity = InvestmentClass('Equity')
    cash = InvestmentClass('Cash')

    xsb = ComponentType("XSB", bond)
    xic = ComponentType("XIC", equity)
    cash_dollars = ComponentType("Cash Dollars", cash)

    rrsp = Account('john RRSP')

    rrsp_xsb = Component(rrsp, xsb, 10000)
    rrsp_xic = Component(rrsp, xic, 10000)
    rrsp_cash = Component(rrsp, cash_dollars, 0)

    bond_allocation = Allocation(bond, 0.4)
    equity_allocation = Allocation(equity, 0.6)
    cash_allocation = Allocation(cash, 0.0)

    allocations = [bond_allocation, equity_allocation, cash_allocation]

    portfolio = Portfolio([rrsp_xsb, rrsp_xic, rrsp_cash])
    component_allocations = portfolio.get_allocations(allocations)
    assert component_allocations[rrsp_xsb] == 0.4
    assert component_allocations[rrsp_xic] == 0.6
    assert component_allocations[rrsp_cash] == 0.0


def test_basic_spouse():
    bond = InvestmentClass('Bond')
    equity = InvestmentClass('Equity')
    cash = InvestmentClass('Cash')

    xsb = ComponentType("XSB", bond)
    xic = ComponentType("XIC", equity)
    cash_dollars = ComponentType("Cash Dollars", cash)

    john_rrsp = Account('john RRSP')
    sue_rrsp = Account('sue RRSP')

    john_rrsp_xsb = Component(john_rrsp, xsb, 10000)
    john_rrsp_xic = Component(john_rrsp, xic, 10000)
    john_rrsp_cash = Component(john_rrsp, cash_dollars, 0)

    sue_rrsp_xsb = Component(sue_rrsp, xsb, 10000)
    sue_rrsp_xic = Component(sue_rrsp, xic, 10000)
    sue_rrsp_cash = Component(sue_rrsp, cash_dollars, 0)

    bond_allocation = Allocation(bond, 0.4)
    equity_allocation = Allocation(equity, 0.6)
    cash_allocation = Allocation(cash, 0.0)

    allocations = [bond_allocation, equity_allocation, cash_allocation]

    portfolio = Portfolio([john_rrsp_xsb, john_rrsp_xic, john_rrsp_cash, sue_rrsp_xsb, sue_rrsp_xic, sue_rrsp_cash])
    component_allocations = portfolio.get_allocations(allocations)
    assert component_allocations[john_rrsp_xsb] == 0.2
    assert component_allocations[john_rrsp_xic] == 0.3
    assert component_allocations[john_rrsp_cash] == 0.0
    assert component_allocations[sue_rrsp_xsb] == 0.2
    assert component_allocations[sue_rrsp_xic] == 0.3
    assert component_allocations[sue_rrsp_cash] == 0.0
