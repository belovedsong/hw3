# Python 3
import cmd
import airimpl

# Decisions/Assumptions:
#
# 1. Selling a ticket expects a row number (in addition to city and date)
# 2. I did not implement any date limits or 30-day limits
# 3. Refund is buggy: seating chart not updated, not checking for past dates


class CntrApp(cmd.Cmd):
    intro = "\nWelcome to the Airline Ticket Console.\nType `help` or `?` to list commands.\n"
    prompt = '> '
    event = None

    def do_q(self, arg):
        """Quit"""
        return True

    def do_EOF(self, arg):
        return True

    def do_remain(self, arg):
        """See remaining seats for a given city and date. Example: `remain BOS 03-30` to see tickets remaining on the flight to BOS on March 30."""
        city, date = arg.split()
        airimpl.remain(city, date)

    def do_sched(self, date):
        """See list of flights for a given date. Example: `sched 03-30`"""
        airimpl.sched(date)

    def do_sell(self, arg):
        """Sell a ticket for a given city, date, and row number. Example: `sell BOS 03-30 12` to sell the next available ticket in row 12 to Boston on March 30."""
        city, date, row = arg.split()
        airimpl.sell(city, date, row)

    def do_status(self, arg):
        """Check ticket status for a given city, date, and row number. Example: `status BOS 03-30 12`"""
        airimpl.status(arg)

    def do_refund(self, arg):
        """Issue a refund given a Ticket ID"""
        airimpl.refund(arg)


if __name__ == '__main__':
    CntrApp().cmdloop()
