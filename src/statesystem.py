"""
.. module:: statesystem
    :platform: Unix, Windows
    :synopsis: Handles states of an entity and calls it's AI.
"""

import events


class StateSystem():
    """Handles states of an entity and calls it's AI.

    :Attributes:
        - *event_manager* (:class:`events.EventManager`): event manager
        - *world* (:class:`gameWorld.GameWorld`): game world contains entities
    """

    def __init__(self, event_manager, world):
        """
        :param event_manager: event manager
        :type event_manager: events.EventManager
        :param world: game world contains entities
        :type world: gameWorld.GameWorld
        """
        self.event_manager = event_manager
        self.event_manager.register_listener(self)

        self.world = world

    def notify(self, event):
        """Notify, when event occurs. 

        :param event: occured event
        :type event: events.Event
        """
        #Update first enemy AI
        for ai in self.world.ai.itervalues():
            ai.current_action(event)
        if isinstance(event, events.TickEvent):
            self.update()
        '''
        if isinstance(event, events.PlayerMoved):
            player_ID = self.world.player 
            if self.world.velocity[player_ID][0] > 0:
                self.world.state[player_ID].walk_left = False
                self.world.state[player_ID].walk_right = True
            elif self.world.velocity[player_ID][0] < 0:
                self.world.state[player_ID].walk_left = True
                self.world.state[player_ID].walk_right = False
        if isinstance(event, events.PlayerStoppedMovement):
            player_ID = self.world.player
            self.world.state[player_ID].walk_left = False
            self.world.state[player_ID].walk_right = False
        '''

    def update(self):
        vel = 7
        #Move entities
        for entity_ID in self.world.state:
            if self.world.velocity[entity_ID]:
                if self.world.state[entity_ID].walk_left:
                    self.world.velocity[entity_ID][0] = -vel
                elif not self.world.state[entity_ID].walk_right:
                    self.world.velocity[entity_ID][0] = 0
                if self.world.state[entity_ID].walk_right:
                    self.world.velocity[entity_ID][0] = vel
                elif not self.world.state[entity_ID].walk_left:
                    self.world.velocity[entity_ID][0] = 0
                if self.world.state[entity_ID].jumping and self.world.state[self.world.player].grounded:
                    self.world.velocity[self.world.player][1] = -vel*2
                    self.world.state[self.world.player].grounded = False
