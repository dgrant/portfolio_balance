def auto_str(cls):
    def __str__(self):
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in vars(self).items())
        )
    cls.__repr__ = __str__
    return cls

@auto_str
class ComponentType(object):
    def __init__(self, name, investmentClass):
        assert type(investmentClass) is InvestmentClass
        self.name = name
        self.investmentClass = investmentClass

@auto_str
class InvestmentClass(object):
    def __init__(self, name):
        self.name = name

@auto_str
class Account(object):
    def __init__(self, name):
        self.name = name

@auto_str
class Component(object):
    def __init__(self, account, componentType, amount):
        assert type(account) is Account
        assert type(componentType) is ComponentType
        self.account = account
        self.componentType = componentType
        self.amount = amount

@auto_str
class Allocation(object):
    def __init__(self, investment_class, amount):
        assert type(investment_class) is InvestmentClass
        assert type(amount) is float
        self.investment_class = investment_class
        self.amount = amount


@auto_str
class Portfolio(object):
    def __init__(self, components):
        assert type(components[0]) is Component
        self.components = components
        print('components: ', components)
        self._get_total_amount_per_class()
        print('total per class: ', self.total_per_class)

    def _get_total_amount_per_class(self):
        print('***** Getting totals per class')
        self.total_per_class = {}
        for component in self.components:
            print('    **** Looking at component: ', component)
            investment_class = component.componentType.investmentClass
            print('    class: ', investment_class)
            if investment_class not in self.total_per_class:
                self.total_per_class[investment_class] = 0
            print('    adding: ', component.amount)
            self.total_per_class[investment_class] += component.amount
            print('    total: ', self.total_per_class[investment_class])

    def balance(self, allocations):
        assert type(allocations[0]) is Allocation
        self._verify_allocations(allocations)

    def get_allocations(self, allocations):
        assert type(allocations[0]) is Allocation
        self._verify_allocations(allocations)
        allocations_by_class = self._load_allocations(allocations)
        ret = {}
        for component in self.components:
            print('***** Looking at component: ', component)
            # Get the class of this part of the portfolio (ie. bond, stock, cash)
            investment_class = component.componentType.investmentClass
            print('Investment class: ', investment_class)
            # Look up the desired allocation of it
            allocation = allocations_by_class[investment_class]
            print('Desired allocation: ', allocation)
            print('Component.amount: ', component.amount)
            print('total per class: ', self.total_per_class[investment_class])
            print('allocation.amount: ', allocation.amount)
            if allocation.amount == 0:
                ret[component] = 0
            else:
                ret[component] = component.amount * allocation.amount / self.total_per_class[investment_class]
            print('desired allocation: ', ret[component])
        return ret

    def _verify_allocations(self, allocations):
        total = sum([x.amount for x in allocations])
        assert total == 1

    def _load_allocations(self, allocations):
        allocations_by_class = {}
        for allocation in allocations:
            investment_class = allocation.investment_class
            if investment_class not in allocations_by_class:
                allocations_by_class[investment_class] = []
            allocations_by_class[investment_class] = allocation
        return allocations_by_class