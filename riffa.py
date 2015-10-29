#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Questo script è stato realizzato per l'estrazione dei premi messi in
palio dall'associazione PerugiaGNULug durante lo svolgimento
dell'evento Linux Day 2015 svoltosi a Magione.
L'elenco dei partecipanti all'estrazione comprende tutti i
partecipanti all'evento registrati in www.eventbrite.it.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
__author__ = 'Marco Rufinelli'
__date__ = '24/10/2015'
__version__ = '0.2'
__licence__ = 'GPLv3'
__copyright__ = 'Copyright 2015, Associazione PerugiaGNULug'

from os import system
from argparse import ArgumentParser
from random import randint
from csv import reader

def _get_parameters():
    """
    Funzione che recupera dalla riga di comando
    i parametri utilizzati dallo script
    """
    parser = ArgumentParser(description='Riffa dello GNULugPerugia')
    parser.add_argument('filename',
                        help='Nomefile CSV')
    parser.add_argument('--ticket_col',
                        type=int,
                        action='store',
                        default=1,
                        help='Colonna Biglietto nel file CVS')
    parser.add_argument('--name_col',
                        type=int,
                        action='store',
                        default=13,
                        help='Colonna Nome nel file CVS')
    parser.add_argument('--surname_col',
                        type=int,
                        action='store',
                        default=14,
                        help='Colonna Cognome nel file CVS')
    parser.add_argument('--max_draws',
                        type=int,
                        action='store',
                        default=0,
                        help='Numero massimo di estrazioni')
    return parser.parse_args()

def _show_header(show_best_wishes):
    """
    Funzione che mostra l'intestazione della riffa
    """
    system('clear')
    print('\n' * 2)
    print('L I N U X D A Y    2 0 1 5'.center(80))
    print('\n' * 2)
    print('E S T R A Z I O N E    B I G L I E T T I'.center(80))
    print('\n' * 3)
    if show_best_wishes:
        print('\n' * 8)
        print('Buona fortuna!  ' .rjust(80))
    raw_input()
    return

def _show_ticket(counter, ticket):
    """
    Funzione che mostra il ticket
    """
    print(' ' * 16 +
          '{:2}° '.format(counter) +
          'estratto: {0}'.format(ticket[0]) +
           '  -  {0}'.format(ticket[1].title()))
    return

def load_tickets(filename, number_col, name_col, surname_col):
    """
    Funziona che carica in un array l'elenco dei
    biglietti e dei corrispondenti nominativi
    che partecipano alla riffa
    """
    tickets=[]
    file = open(filename, 'r')
    csv_text = reader(file, delimiter=',', quotechar='"')
    for row in csv_text:
        if row[number_col].isdigit():
            tickets.append((row[number_col],
                            "{0} {1}".format(row[name_col], row[surname_col])))
    file.close()
    return tickets

def draw(tickets):
    """
    Funziona che esegue l'estrazione dei
    biglietti e ne mostra il risultato
    """
    ticket = tickets[randint(0, len(tickets) - 1)]
    tickets.remove(ticket)
    return ticket

if __name__ == '__main__':
    args = _get_parameters()
    _show_header(True)
    ticket_list = load_tickets(filename = args.filename,
                               number_col = args.ticket_col,
                               name_col = args.name_col,
                               surname_col = args.surname_col)

    _show_header(False)
    counter = 1
    while(len(ticket_list) > 0
          and (counter <= args.max_draws
               or args.max_draws == 0)):
        _show_ticket(counter, draw(ticket_list))
        raw_input()
        counter += 1
