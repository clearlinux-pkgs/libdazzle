#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libdazzle
Version  : 3.32.1
Release  : 13
URL      : https://download.gnome.org/sources/libdazzle/3.32/libdazzle-3.32.1.tar.xz
Source0  : https://download.gnome.org/sources/libdazzle/3.32/libdazzle-3.32.1.tar.xz
Summary  : A library to delight your users with fancy features
Group    : Development/Tools
License  : GPL-3.0
Requires: libdazzle-bin = %{version}-%{release}
Requires: libdazzle-data = %{version}-%{release}
Requires: libdazzle-lib = %{version}-%{release}
Requires: libdazzle-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : vala

%description
# Dazzle
The libdazzle library is a companion library to GObject and Gtk+.
It provides various features that we wish were in the underlying library but cannot for various reasons.
In most cases, they are wildly out of scope for those libraries.
In other cases, our design isn't quite generic enough to work for everyone.

%package bin
Summary: bin components for the libdazzle package.
Group: Binaries
Requires: libdazzle-data = %{version}-%{release}
Requires: libdazzle-license = %{version}-%{release}

%description bin
bin components for the libdazzle package.


%package data
Summary: data components for the libdazzle package.
Group: Data

%description data
data components for the libdazzle package.


%package dev
Summary: dev components for the libdazzle package.
Group: Development
Requires: libdazzle-lib = %{version}-%{release}
Requires: libdazzle-bin = %{version}-%{release}
Requires: libdazzle-data = %{version}-%{release}
Provides: libdazzle-devel = %{version}-%{release}
Requires: libdazzle = %{version}-%{release}

%description dev
dev components for the libdazzle package.


%package lib
Summary: lib components for the libdazzle package.
Group: Libraries
Requires: libdazzle-data = %{version}-%{release}
Requires: libdazzle-license = %{version}-%{release}

%description lib
lib components for the libdazzle package.


%package license
Summary: license components for the libdazzle package.
Group: Default

%description license
license components for the libdazzle package.


%prep
%setup -q -n libdazzle-3.32.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557014744
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libdazzle
cp COPYING %{buildroot}/usr/share/package-licenses/libdazzle/COPYING
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dazzle-list-counters

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Dazzle-1.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/vala/vapi/libdazzle-1.0.deps
/usr/share/vala/vapi/libdazzle-1.0.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/libdazzle-1.0/actions/dzl-action-group.h
/usr/include/libdazzle-1.0/actions/dzl-child-property-action.h
/usr/include/libdazzle-1.0/actions/dzl-properties-group.h
/usr/include/libdazzle-1.0/actions/dzl-settings-flag-action.h
/usr/include/libdazzle-1.0/actions/dzl-widget-action-group.h
/usr/include/libdazzle-1.0/animation/dzl-animation.h
/usr/include/libdazzle-1.0/animation/dzl-box-theatric.h
/usr/include/libdazzle-1.0/animation/dzl-frame-source.h
/usr/include/libdazzle-1.0/app/dzl-application-window.h
/usr/include/libdazzle-1.0/app/dzl-application.h
/usr/include/libdazzle-1.0/bindings/dzl-binding-group.h
/usr/include/libdazzle-1.0/bindings/dzl-signal-group.h
/usr/include/libdazzle-1.0/cache/dzl-task-cache.h
/usr/include/libdazzle-1.0/dazzle.h
/usr/include/libdazzle-1.0/dzl-enums.h
/usr/include/libdazzle-1.0/dzl-version-macros.h
/usr/include/libdazzle-1.0/dzl-version.h
/usr/include/libdazzle-1.0/files/dzl-directory-model.h
/usr/include/libdazzle-1.0/files/dzl-directory-reaper.h
/usr/include/libdazzle-1.0/files/dzl-file-transfer.h
/usr/include/libdazzle-1.0/files/dzl-recursive-file-monitor.h
/usr/include/libdazzle-1.0/graphing/dzl-cpu-graph.h
/usr/include/libdazzle-1.0/graphing/dzl-cpu-model.h
/usr/include/libdazzle-1.0/graphing/dzl-graph-column.h
/usr/include/libdazzle-1.0/graphing/dzl-graph-line-renderer.h
/usr/include/libdazzle-1.0/graphing/dzl-graph-model.h
/usr/include/libdazzle-1.0/graphing/dzl-graph-renderer.h
/usr/include/libdazzle-1.0/graphing/dzl-graph-view.h
/usr/include/libdazzle-1.0/menus/dzl-joined-menu.h
/usr/include/libdazzle-1.0/menus/dzl-menu-button.h
/usr/include/libdazzle-1.0/menus/dzl-menu-manager.h
/usr/include/libdazzle-1.0/panel/dzl-dock-bin-edge.h
/usr/include/libdazzle-1.0/panel/dzl-dock-bin.h
/usr/include/libdazzle-1.0/panel/dzl-dock-item.h
/usr/include/libdazzle-1.0/panel/dzl-dock-manager.h
/usr/include/libdazzle-1.0/panel/dzl-dock-overlay-edge.h
/usr/include/libdazzle-1.0/panel/dzl-dock-overlay.h
/usr/include/libdazzle-1.0/panel/dzl-dock-paned.h
/usr/include/libdazzle-1.0/panel/dzl-dock-revealer.h
/usr/include/libdazzle-1.0/panel/dzl-dock-stack.h
/usr/include/libdazzle-1.0/panel/dzl-dock-transient-grab.h
/usr/include/libdazzle-1.0/panel/dzl-dock-types.h
/usr/include/libdazzle-1.0/panel/dzl-dock-widget.h
/usr/include/libdazzle-1.0/panel/dzl-dock-window.h
/usr/include/libdazzle-1.0/panel/dzl-dock.h
/usr/include/libdazzle-1.0/panel/dzl-tab-strip.h
/usr/include/libdazzle-1.0/panel/dzl-tab.h
/usr/include/libdazzle-1.0/pathbar/dzl-path-bar.h
/usr/include/libdazzle-1.0/pathbar/dzl-path-element.h
/usr/include/libdazzle-1.0/pathbar/dzl-path.h
/usr/include/libdazzle-1.0/prefs/dzl-preferences-bin.h
/usr/include/libdazzle-1.0/prefs/dzl-preferences-entry.h
/usr/include/libdazzle-1.0/prefs/dzl-preferences-file-chooser-button.h
/usr/include/libdazzle-1.0/prefs/dzl-preferences-flow-box.h
/usr/include/libdazzle-1.0/prefs/dzl-preferences-font-button.h
/usr/include/libdazzle-1.0/prefs/dzl-preferences-group.h
/usr/include/libdazzle-1.0/prefs/dzl-preferences-page.h
/usr/include/libdazzle-1.0/prefs/dzl-preferences-spin-button.h
/usr/include/libdazzle-1.0/prefs/dzl-preferences-switch.h
/usr/include/libdazzle-1.0/prefs/dzl-preferences-view.h
/usr/include/libdazzle-1.0/prefs/dzl-preferences.h
/usr/include/libdazzle-1.0/search/dzl-fuzzy-index-builder.h
/usr/include/libdazzle-1.0/search/dzl-fuzzy-index-cursor.h
/usr/include/libdazzle-1.0/search/dzl-fuzzy-index-match.h
/usr/include/libdazzle-1.0/search/dzl-fuzzy-index.h
/usr/include/libdazzle-1.0/search/dzl-fuzzy-mutable-index.h
/usr/include/libdazzle-1.0/search/dzl-levenshtein.h
/usr/include/libdazzle-1.0/search/dzl-pattern-spec.h
/usr/include/libdazzle-1.0/search/dzl-trie.h
/usr/include/libdazzle-1.0/settings/dzl-settings-sandwich.h
/usr/include/libdazzle-1.0/shortcuts/dzl-shortcut-accel-dialog.h
/usr/include/libdazzle-1.0/shortcuts/dzl-shortcut-chord.h
/usr/include/libdazzle-1.0/shortcuts/dzl-shortcut-context.h
/usr/include/libdazzle-1.0/shortcuts/dzl-shortcut-controller.h
/usr/include/libdazzle-1.0/shortcuts/dzl-shortcut-label.h
/usr/include/libdazzle-1.0/shortcuts/dzl-shortcut-manager.h
/usr/include/libdazzle-1.0/shortcuts/dzl-shortcut-model.h
/usr/include/libdazzle-1.0/shortcuts/dzl-shortcut-phase.h
/usr/include/libdazzle-1.0/shortcuts/dzl-shortcut-simple-label.h
/usr/include/libdazzle-1.0/shortcuts/dzl-shortcut-theme-editor.h
/usr/include/libdazzle-1.0/shortcuts/dzl-shortcut-theme.h
/usr/include/libdazzle-1.0/shortcuts/dzl-shortcut-tooltip.h
/usr/include/libdazzle-1.0/shortcuts/dzl-shortcuts-group.h
/usr/include/libdazzle-1.0/shortcuts/dzl-shortcuts-section.h
/usr/include/libdazzle-1.0/shortcuts/dzl-shortcuts-shortcut.h
/usr/include/libdazzle-1.0/shortcuts/dzl-shortcuts-window.h
/usr/include/libdazzle-1.0/statemachine/dzl-state-machine-buildable.h
/usr/include/libdazzle-1.0/statemachine/dzl-state-machine.h
/usr/include/libdazzle-1.0/suggestions/dzl-suggestion-entry-buffer.h
/usr/include/libdazzle-1.0/suggestions/dzl-suggestion-entry.h
/usr/include/libdazzle-1.0/suggestions/dzl-suggestion-popover.h
/usr/include/libdazzle-1.0/suggestions/dzl-suggestion-row.h
/usr/include/libdazzle-1.0/suggestions/dzl-suggestion.h
/usr/include/libdazzle-1.0/theming/dzl-css-provider.h
/usr/include/libdazzle-1.0/theming/dzl-theme-manager.h
/usr/include/libdazzle-1.0/tree/dzl-list-store-adapter.h
/usr/include/libdazzle-1.0/tree/dzl-tree-builder.h
/usr/include/libdazzle-1.0/tree/dzl-tree-node.h
/usr/include/libdazzle-1.0/tree/dzl-tree-types.h
/usr/include/libdazzle-1.0/tree/dzl-tree.h
/usr/include/libdazzle-1.0/util/dzl-cairo.h
/usr/include/libdazzle-1.0/util/dzl-cancellable.h
/usr/include/libdazzle-1.0/util/dzl-counter.h
/usr/include/libdazzle-1.0/util/dzl-date-time.h
/usr/include/libdazzle-1.0/util/dzl-dnd.h
/usr/include/libdazzle-1.0/util/dzl-file-manager.h
/usr/include/libdazzle-1.0/util/dzl-gdk.h
/usr/include/libdazzle-1.0/util/dzl-gtk.h
/usr/include/libdazzle-1.0/util/dzl-heap.h
/usr/include/libdazzle-1.0/util/dzl-int-pair.h
/usr/include/libdazzle-1.0/util/dzl-list-model-filter.h
/usr/include/libdazzle-1.0/util/dzl-macros.h
/usr/include/libdazzle-1.0/util/dzl-pango.h
/usr/include/libdazzle-1.0/util/dzl-read-only-list-model.h
/usr/include/libdazzle-1.0/util/dzl-rgba.h
/usr/include/libdazzle-1.0/util/dzl-ring.h
/usr/include/libdazzle-1.0/util/dzl-variant.h
/usr/include/libdazzle-1.0/widgets/dzl-bin.h
/usr/include/libdazzle-1.0/widgets/dzl-bolding-label.h
/usr/include/libdazzle-1.0/widgets/dzl-box.h
/usr/include/libdazzle-1.0/widgets/dzl-centering-bin.h
/usr/include/libdazzle-1.0/widgets/dzl-column-layout.h
/usr/include/libdazzle-1.0/widgets/dzl-counters-window.h
/usr/include/libdazzle-1.0/widgets/dzl-elastic-bin.h
/usr/include/libdazzle-1.0/widgets/dzl-empty-state.h
/usr/include/libdazzle-1.0/widgets/dzl-entry-box.h
/usr/include/libdazzle-1.0/widgets/dzl-file-chooser-entry.h
/usr/include/libdazzle-1.0/widgets/dzl-list-box-row.h
/usr/include/libdazzle-1.0/widgets/dzl-list-box.h
/usr/include/libdazzle-1.0/widgets/dzl-multi-paned.h
/usr/include/libdazzle-1.0/widgets/dzl-pill-box.h
/usr/include/libdazzle-1.0/widgets/dzl-priority-box.h
/usr/include/libdazzle-1.0/widgets/dzl-progress-button.h
/usr/include/libdazzle-1.0/widgets/dzl-progress-icon.h
/usr/include/libdazzle-1.0/widgets/dzl-progress-menu-button.h
/usr/include/libdazzle-1.0/widgets/dzl-radio-box.h
/usr/include/libdazzle-1.0/widgets/dzl-scrolled-window.h
/usr/include/libdazzle-1.0/widgets/dzl-search-bar.h
/usr/include/libdazzle-1.0/widgets/dzl-simple-label.h
/usr/include/libdazzle-1.0/widgets/dzl-simple-popover.h
/usr/include/libdazzle-1.0/widgets/dzl-slider.h
/usr/include/libdazzle-1.0/widgets/dzl-stack-list.h
/usr/include/libdazzle-1.0/widgets/dzl-three-grid.h
/usr/lib64/libdazzle-1.0.so
/usr/lib64/pkgconfig/libdazzle-1.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libdazzle-1.0.so.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libdazzle/COPYING
