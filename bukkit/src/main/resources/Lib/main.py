import pyspigot as ps
from java.util import Properties
from java.io import FileInputStream
from org.bukkit.event.player import AsyncPlayerChatEvent
from org.bukkit.event import EventPriorityq
from org.bukkit.entity import Player
from org.bukkit import ChatColorfrom dev.magicmq.pyspigot.manager.task import TaskManager
from dev.magicmq.pyspigot.manager.config import ConfigManager
from dev.magicmq.pyspigot.manager.database import DatabaseManager
from dev.magicmq.pyspigot.manager.redis import RedisManager
from org.bukkit.event.player import PlayerJoinEvent
from org.bukkit import Bukkit
from org.bukkit import ChatColor


props = Properties()
props.load(FileInputStream("config.properties"))

db_url = props.getProperty("database.url")
db_user = props.getProperty("database.user")
db_password = props.getProperty("database.password")


def join_event(event):
    player = event.getPlayer()
    if player.hasPermission('joinmessage.permission'):
        notify_admins(player)
        if message_delay > 0:
            ps.scheduler.runTaskLater(lambda: player.sendMessage(ChatColor.translateAlternateColorCodes('&', join_message)), message_delay)
        else:
            player.sendMessage(ChatColor.translateAlternateColorCodes('&', join_message))

def notify_admins(joined):
    for player in Bukkit.getOnlinePlayers():
        if player.hasPermission('joinmessage.admin'):
            player.sendMessage(ChatColor.translateAlternateColorCodes('&', join_notify_message.replace('%player%', joined.getName())))

ps.listener.registerListener(join_event, PlayerJoinEvent)


def task():
    for player in Bukkit.getOnlinePlayers():
        player.sendMessage(ChatColor.translateAlternateColorCodes('&', message))

task_id = ps.scheduler.scheduleRepeatingTask(task, 0, 100)

